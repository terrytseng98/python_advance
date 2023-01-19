import urequests as req
from hcsr04 import HCSR04
from machine import Pin, ADC, PWM, UART
from mcu_def import gpio, mcu_fun
import dht
import time
import json

adc = ADC(0)
mcu = mcu_fun()
mcu.connect_ap("SingularClass0", "Singular#1234")
mcu.mqtt_subscribe(mq_id='Ray')
mcu.mp3_initial()
lcd = mcu.lcd_initial(scl_pin=gpio.D1, sda_pin=gpio.D2)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
sensor = HCSR04(trigger_pin=gpio.SDD2, echo_pin=gpio.SDD2)
sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)
earthquake = Pin(gpio.SDD3, Pin.IN)
IR = Pin(gpio.D3, Pin.IN)
msg_json = {}
apiURL = 'http://api.thingspeak.com/update?key={}'.format('3M37UWM34GTNMHEG')
cnt = 0


def push_data(data):
    send_str = ""
    data = list(data.values())
    for i in range(len(data)):
        send_str += ("&field" + str(i + 1) + "=" + str(data[i]))

    print(send_str)

    r = req.get(apiURL + send_str)

    if r.status_code != 200:
        print('Bad request')
    elif r.text == '0':
        print('get request but not push data successfully')
    else:
        print('Data saved, id: ', r.text)


while True:
    distance = sensor.distance_cm()
    light_value = adc.read()
    d.measure()  # 讀取溫溼度
    temp = d.temperature()  # 將溫溼度分別存在不同變數
    hum = d.humidity()
    msg_json["humidity"] = hum
    msg_json["temperature"] = temp
    msg_json["lightsensor"] = light_value
    # msg_json["distance"] = distance
    msg_json["earthquake"] = earthquake.value()
    msg_json["IR"] = IR.value()
    mcu.mqtt_put_msg(topic='Ray', msg=json.dumps(msg_json))

    if distance <= 5:
        mcu.servo_angle(sg_pin, 0)
    else:
        mcu.servo_angle(sg_pin, 80)

    if int(earthquake.value()) == 1:
        mcu.mp3_start()
    elif IR.value() == 1:
        mcu.mp3_start()

    time.sleep(1)
    cnt += 1
    if cnt >= 13:
        cnt = 0
        push_data(msg_json)
