import requests, json
import matplotlib.pyplot as plt
from tkinter import *

base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

def clear():
    status.config(text="")
def get():
    response = requests.get(base_url)
    info = response.json()

    area=pos_info.get()
    show_info=""

    position=[]
    total_bike=[]
    remain_bike=[]

    for i in range(1, len(info["retVal"])):
        num=("%04d"%i)
        if num in info["retVal"].keys() and info["retVal"][num]["sarea"]==area:
            position.append(info["retVal"][num]["sna"].split("(")[0])
            total_bike.append(int(info["retVal"][num]["tot"]))
            remain_bike.append(int(info["retVal"][num]["sbi"]))
            
    for i in range(1, len(position)):       
        show_info+=("%s 總共車輛=%d 剩餘車輛=%d\n" %(position[i], total_bike[i], remain_bike[i]))

    status.config(text=show_info)

    plt.plot(position, total_bike, "r-o", label="總共車輛")
    plt.plot(position, remain_bike,"g--", label="剩餘車輛")
    plt.legend(loc="best")
    plt.show()
    
windows = Tk()
windows.title('gui')

pos=Label(windows,text='請輸入區名', font=('Arial', 12))
pos.pack()

pos_info=Entry(windows)
pos_info.pack()

status=Label(windows, text='')
status.pack()

btn=Button(windows, text="獲取Youbike資料", command=get, bg="red")
btn.pack()

btn=Button(windows, text="清除Youbike資料", command=clear, bg="red")
btn.pack()

windows.mainloop()