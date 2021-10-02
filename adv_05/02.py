import requests, json
from tkinter import *
api_key = "2f7671995fd280c1b8c10843d66b3f93"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
units = "metric"
lang = "zh_tw"
def get_weather():
    city_name = city_info.get()
    send_url = base_url
    send_url += "appid=" + api_key
    send_url += "&q=" + city_name
    send_url += "&units=" + units
    send_url += "&lang=" + lang
    print ("%s\n" % send_url)
    response = requests.get (send_url)
    info = response.json()
    print(info)
    if "main" in info.keys():
        temp_info = info ["main"]
        current_temp = temp_info["temp"]
        weather_info = info["weather"][0]
        weather_desc = weather_info["description" ]
        put_city.config(text="city = " + city_name)
        put_temp.config( text="Temperature = " + str(current_temp))
        put_disc.config( text="Description = " + str(weather_desc))
    else:
        put_city.config(text="City Not Found ")
windows = Tk()
windows.title("My Weather")
put_city = Label(windows, text="")
put_city.pack()
put_temp = Label(windows, text="")
put_temp.pack()
put_disc = Label(windows, text="")
put_disc.pack()
city_info = Entry(windows, text="")
city_info.pack()
btn = Button(windows, text='獲取天氣資料' , command=get_weather)
btn.pack()
windows.mainloop()