import requests, json
import matplotlib.pyplot as plt

base_url = "https://data.epa.gov.tw/api/v1/"
api_num = "aqx_p_432?"

offset = "0"
limit = "50"
api_key = "a3637ceb-0a38-454a-af35-538dd301e5a4"

base_url = "https://data.epa.gov.tw/api/v1/"
api_num = "aqx_p_432?"
offset = "0"
limit = "50"
api_key = "a3637ceb-0a38-454a-af35-538dd301e5a4"
send_url = base_url
send_url += api_num
send_url += "offset=" + offset
send_url += "&limit=" + limit
send_url += "&api_key=" + api_key
print(send_url)

response = requests.get(send_url)
info = json.loads(response.text)

if "fields" in info.keys():
    aqi_value = []
    aqi_posit = []
    aqi_pm2_5 = []
    for i in range(int(limit)):
        data = info["records"][i]["County"]
        #print(data)

        if data == "臺北市":
            aqi_posit.append( info[ "records"][i]["SiteName"])
            aqi_value.append(info["records"][i]["AQI"])
            aqi_pm2_5.append(info[ "records"][i] ["PM2.5"])
            
    plt.plot(aqi_posit, aqi_value, "r-o", label="AQI")
    plt.plot(aqi_posit, aqi_pm2_5,"g-",label="PM2.5")
    plt.legend(loc="upper left")
    plt.show()
else:
    print("Found Error")