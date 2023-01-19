@echo off
cd %USERPROFILE%\.vscode\extensions\rt*
xcopy %0\..\cpy %1 /Y /S
