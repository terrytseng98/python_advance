import requests, json
import matplotlib.pyplot as plt
from tkinter import *

def get_pm25():
    send_url = base_url
    send_url += api_num
    send_url += "offset=" + offset
    send_url += "&limit=" + limit
    send_url += "&api_key=" + api_key
   # print("%s\n"%send_url)

    response = requests.get(send_url)
    info = json.loads(response.text)

    city=pos_info.get()

    if "fields" in info.keys():
        aqi_value = []
        aqi_posit = []
        aqi_pm2_5 = []
        for i in range(int(limit)):
            data = info["records"][i]["County"]
            #print(data)
            if data==city:
                aqi_posit.append(info["records"][i]["SiteName"])
                aqi_value.append(int(info["records"][i]["AQI"]))
                aqi_pm2_5.append(int(info["records"][i]["PM2.5"]))
                
        show_info=""
        for i in range(len(aqi_value)):
            show_info+=("%s AQI%d PM2.5=%d\n"%(aqi_posit[i], aqi_value[i], aqi_pm2_5[i]))

        status.config(text=show_info)

        plt.plot(aqi_posit, aqi_value, "c-s", label="AQI")
        plt.plot(aqi_posit, aqi_pm2_5,"r-^",label="PM2.5")
        plt.legend(loc="best")
        plt.show()
    else:
        print("Found Error")

windows = Tk()
windows.title('空氣品質')

base_url = "https://data.epa.gov.tw/api/v1/"
api_num = "aqx_p_432?"
offset = "0"
limit = "50"
api_key = "a3637ceb-0a38-454a-af35-538dd301e5a4"

pos=Label(windows,text='請輸入城市名稱', font=('Arial', 12))
pos.pack()
pos_info=Entry(windows)
pos_info.pack()

status=Label(windows, text='')
status.pack()

btn=Button(windows, text="獲取城市空氣品質", command=get_pm25, bg="red")
btn.pack()

windows.mainloop()