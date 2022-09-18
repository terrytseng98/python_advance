import requests, json
import matplotlib.pyplot as plt
api_key = "2f7671995fd280c1b8c10843d66b3f93"
base_url = "https://api.openweathermap.org/data/2.5/onecall?"
lat = "25"
#lat = input("Enter latitude:")
lon = "125" #lon = input("Enter longitude:")
exclude = "minutely, hourly"
units = "metric"
lang = "zh_tw"

send_url = base_url
send_url += "lat=" + lat
send_url += "&lon=" + lon
send_url += "&exclude=" + exclude

send_url += "&appid=" + api_key
send_url += "&units=" + units
send_url += "&lang=" + lang
print("%s\n" % send_url)

response = requests.get (send_url)
info = json.loads(response.text)
#print(info)

temp_days = []
if "lat" in info.keys():
    for i in range (7):
        temps = info["daily"][i]["temp"]["day"]
        temp_days.append (temps)
        print ("Day%d Temp=%s C" % (i, info["daily"][i]["temp"]["day"]))

    plt.plot(range(1, 8), temp_days)
    plt.show()
else:
    print("Request Fail")