data = {
    "coord": {"lon": 121.5319,"lat": 25.0478},
    "weather": [{"status": "Clouds"},{"des": "多雲"}],
    "temperature": [{   "temp": 32.47,"temp_min": 30.6,"temp_max": 33.93}],
    "name": "Taipei",
    }
key_name=input('Find key:')
if key_name in data.keys():
    if (key_name == "coord") :
    print ("lon = %s" %% data[key_name] ["lon"] )
    print ("lat = %s" %% data[key_name] ["lat"] )
    elif (key_name == "weather") :
    print("status = %s" %% data[key_name][] ["status"])
    print("des= %s" %% data[key_name] [1] ["des"])
    elif (key_name == "temperature"):
    print("temp = %s" % data[key_name] [] ["temp"])
    print ("temp_min = %s" % data[key_name] [] ["temp_min" ])
    print("temp_max = %s" % data[key_name] [] ["temp_max" ])
    elif (key_name == "name") :
        print("name = %s" % data[key_name ] )
    else:
        print ("Not find")
