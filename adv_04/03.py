import requests

api_key = "2f7671995fd280c1b8c10843d66b3f93"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
units = "metric"
lang = "zh_tw"

send_url = base_url
send_url += "appid=" + api_key
send_url += "&q=" + city_name
send_url += "&units=" + units
send_url += "&lang=" + lang

print("%s\n" % send_url)
response = requests.get(send_url)
info = response.json()
print(info)
print(info['weather'][0]["description"])
print(info['main']["temp"])