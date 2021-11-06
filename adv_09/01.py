import requests, json

base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

response = requests.get(base_url)
info = response.json()
#print(info)

for i in range(1, 11):
    num=("%04d"%i)
    if info["retVal"][num]:
        print("地點:%s" % info["retVal"][num]["sna"].split("(")[0])
        print("總共車輛:%s" % int (info["retVal"][num]["tot"]))
        print("目前停車數量:%s\n" % int (info["retVal"][num]["sbi"]))