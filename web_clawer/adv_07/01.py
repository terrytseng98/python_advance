import requests, json

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
city="板橋"

if "fields" in info.keys():
    for i in range(int(limit)):
        data = info["records"][i]["SiteName"]
        #print(data)
        if data==city:
            print("City=" + info["records"][i]["County"])
            print("SiteName=" + info["records"][i]["SiteName"])
            print("AQI=" + info["records"][i]["AQI"])
            print("PM2.5=" + info["records"][i]["PM2.5"])
            print("Status= " + info["records"][i]["Status"] + "\n")
else:
    print("Found Error ")
