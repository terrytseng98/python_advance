const vscode = require("vscode");
const cp = require('child_process');
const iconv = require('iconv-lite');
const fs = require('fs');
const os = require('os');
const languageLocalize = require("../language/index");
var terminalsObj = {};
var isDownloading = false;
var lineBreak = os.type() == "Windows_NT" ? '\r\n' : '\n';

module.exports = function (context) {
    context.globalState.update('micropython.isDownloading',isDownloading );
    vscode.commands.registerCommand("extension.downloadFile", function (selectedItem) {
        //如果正在同步或者正在运行或者正在下载，则不下载文件
        var isRuning = context.globalState.get('micropython.isRuning');
        var isSyncing = context.globalState.get('micropython.isSyncing');
        var isDownloading = context.globalState.get('micropython.isDownloading');

        if(isRuning || isDownloading || isSyncing ){
            return;
        }
        isDownloading = true;
        context.globalState.update('micropython.isDownloading',isDownloading );
        
        if(selectedItem && selectedItem.fsPath){
            var fsPath = selectedItem.fsPath.replace(/\\/g,"/");
            let fsStats = fs.statSync(fsPath);
            if(fsStats.isFile()){
                vscode.window.showTextDocument(vscode.Uri.file(fsPath));
            }
            setTimeout(function(){
                if(fsStats.isFile()){
                    vscode.window.activeTextEditor.document.save();
                }
                var allDevices = JSON.parse(context.globalState.get('adb.devices'));
                var connectedDevices = allDevices.filter(function (item) {
                    return item.connected;
                })
                //quickpick 面板配置
                var options = [];
                if (connectedDevices.length <= 0) {
                    isDownloading = false;
                    context.globalState.update('micropython.isDownloading',isDownloading );
                    options = [
                        {
                            label: languageLocalize("micropython.execute.noDeviceConnected")
                        }
                    ]
                } else if (connectedDevices.length == 1) {
                    // executeLines(connectedDevices[0].id.replace(/:\d+/g, ""),text)
                    download(connectedDevices[0].id.replace(/:\d+/g, ""),fsPath)
                    return;
                } else {
                    options = connectedDevices.map(function (item) {
                        var tip = languageLocalize("micropython.execute.clickToRun");
                        return {
                            label: item.id.replace(/:\d+/g, ""),
                            description: tip,
                            connected: item.connected,
                            type: item.type
                        }
                    })
                }
        
                const quickPick = vscode.window.createQuickPick();
                quickPick.items = options;
                quickPick.onDidChangeSelection(selection => {
                    if (selection[0]) {
                        if (selection[0].label == languageLocalize("micropython.execute.noDeviceConnected")) {
                            quickPick.hide();
                            isDownloading = false;
                            context.globalState.update('micropython.isDownloading',isDownloading );
                            return;
                        } else {
                            // executeLines(selection[0].label.replace(/:\d+/g, ""), text)
                            download(selection[0].label.replace(/:\d+/g, ""),fsPath)
                            quickPick.hide();
                        }
                    } else {
                        isDownloading = false;
                        context.globalState.update('micropython.isDownloading',isDownloading );
                        return;
                    }
                });
                quickPick.onDidHide(() => quickPick.dispose());
                quickPick.show();
            },200)
        }else{
            isDownloading = false;
            context.globalState.update('micropython.isDownloading',isDownloading );
        }

        function download(itemId,fsPath){
            //执行文件提示
            var executeButtonConfig = vscode.workspace.getConfiguration().get("MicroPython.syncButton");
            executeButtonConfig[0].text = "$(sync~spin)";
            vscode.workspace.getConfiguration().update("MicroPython.syncButton",executeButtonConfig);
            
            var extensionPath = vscode.extensions.getExtension('RT-Thread.rt-thread-micropython').extensionPath.replace(/\\/g,'/');
            var pythonPath;
            //如果是串口设备
            if(/^COM/.test(itemId) || /^\/dev/.test(itemId)){
                var allTerminals = vscode.window.terminals;
                allTerminals.forEach(function(item){
                    terminalsObj[item.name] = item;
                })
                for(var key in terminalsObj){
                    var flag = true;
                    allTerminals.forEach(function(item){
                        if(item.name == key){
                            flag = false;
                        }
                    })
                    if(flag){
                        delete terminalsObj[key]
                    }
                }    

                if(os.type() == "Windows_NT"){
                    pythonPath =  extensionPath + "/ampy/cli.exe";
                }else if(os.type() == "Linux"){
                    pythonPath =  extensionPath + "/ampy/cli";
                }else{
                    pythonPath =  extensionPath + "/ampy/cli_mac";
                }
                if(terminalsObj[itemId]){
                    terminalsObj[itemId].sendText(`${String.fromCharCode(24)}`,false);
                };
                cp.exec(`"${pythonPath}" -p ${itemId} -d 5 put "${fsPath}"`,{ encoding: 'binary' }, (error, stdout) => {
                    if(!error){
                        var res = iconv.decode(Buffer.alloc(stdout.toString().length, stdout.toString(), 'binary'), 'cp936');
                        console.log(res);
                        openRepl(itemId);
                        vscode.window.showInformationMessage(languageLocalize("micropython.downloadFile.downloadFileSuccessful"));
                        isDownloading = false;
                        context.globalState.update('micropython.isDownloading',isDownloading );
                        executeButtonConfig[0].text = "$(sync)";
                        vscode.workspace.getConfiguration().update("MicroPython.syncButton",executeButtonConfig);
                    }else{
                        openRepl(itemId)
                        var err = iconv.decode(Buffer.alloc(error.toString().length, error.toString(), 'binary'), 'cp936');
                        console.log(err)
                        var errMessage = err.replace(/[\s\r\n]/g,"");
                        if(errMessage.indexOf("ThisisnotaMicroPythonboard") !== -1){
                            vscode.window.showInformationMessage(languageLocalize("micropython.execute.notMicroPythonBoard"));
                        }else if(errMessage.indexOf("Theuosmoduleisnotenabled") !== -1){
                            vscode.window.showInformationMessage(languageLocalize("micropython.execute.uosModuleFailed"));
                        }else if(errMessage.indexOf("failedtoaccess") !== -1){
                            vscode.window.showInformationMessage( itemId + languageLocalize("micropython.execute.failedtoAccess"));
                        }else{
                            vscode.window.showInformationMessage(languageLocalize("micropython.execute.executeFailed"));
                        }
                        isDownloading = false;
                        context.globalState.update('micropython.isDownloading',isDownloading );
                        executeButtonConfig[0].text = "$(sync)";
                        vscode.workspace.getConfiguration().update("MicroPython.syncButton",executeButtonConfig);
                    }
    
                })

            }else{
                isDownloading = false;
                context.globalState.update('micropython.isDownloading',isDownloading );
                executeButtonConfig[0].text = "$(sync)";
                vscode.workspace.getConfiguration().update("MicroPython.syncButton",executeButtonConfig);
                return;
            }
            

        }

        function openRepl(itemId){
            var nameId = itemId;
            var flag = true;
            for(var key in terminalsObj){
                if(key == nameId){
                    flag = false;
                }
            }
            var extensionPath = vscode.extensions.getExtension('RT-Thread.rt-thread-micropython').extensionPath.replace(/\\/g,'/');
            var pythonPath = extensionPath + "/ampy";
            var pythonExe;
            if(os.type() == "Windows_NT"){
                pythonExe = "cli.exe";
            }else if(os.type() == "Linux"){
                pythonExe = `"${extensionPath}/ampy/cli"`;
            }else{
                pythonExe = `"${extensionPath}/ampy/cli_mac"`;
            }
            if(flag){
                terminalsObj[nameId] =  vscode.window.createTerminal({ name: nameId });
                terminalsObj[nameId].show();
                terminalsObj[nameId].sendText(`${lineBreak}`)
                terminalsObj[nameId].sendText(`Set-ItemProperty HKCU:\Console VirtualTerminalLevel -Type DWORD 1`)
                terminalsObj[nameId].sendText( `$env:Path+=";${pythonPath}"`)
                terminalsObj[nameId].sendText(`${lineBreak}`)
                terminalsObj[nameId].sendText(`clear${lineBreak}`)
                setTimeout(function(){
                    terminalsObj[nameId].sendText(`${pythonExe} -p ${nameId} repl`);
                },100)
            }else{
                terminalsObj[nameId].show();
                setTimeout(function(){
                    terminalsObj[nameId].sendText(`${pythonExe} -p ${nameId} repl`);
                },100)
            }
    
        }

       

    })


}