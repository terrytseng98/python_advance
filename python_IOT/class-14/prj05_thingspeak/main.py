from time import sleep
import urequests as req
from mcu_def import mcu_fun

mcu = mcu_fun()
mcu.connect_ap("SingularClass0", "Singular#1234")
apiURL = 'http://api.thingspeak.com/update?key={}'.format('3M37UWM34GTNMHEG')

d = {"field1": 10}
send_str = ""

for key, value in d.items():
    send_str += ("&" + key + "=" + str(value))

print(send_str)

while True:
    r = req.get(apiURL + send_str)
    if r.status_code != 200:
        print('Bad request')
    elif r.text == '0':
        print('get request but not push data successfully')
    else:
        print('Data saved, id: ', r.text)
    sleep(20)
