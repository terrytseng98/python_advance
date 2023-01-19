from hcsr04 import HCSR04
from machine import Pin, ADC, PWM
from mcu_def import gpio, mcu_fun
import dht
import time
import json

adc = ADC(0)
mcu = mcu_fun()
mcu.connect_ap("SingularClass0", "Singular#1234")
mcu.mqtt_subscribe(mq_id='Ray')
# lcd = mcu.lcd_initial(scl_pin=gpio.D1, sda_pin=gpio.D2)
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
sensor = HCSR04(trigger_pin=gpio.SDD2, echo_pin=gpio.SDD2)
sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)
earthquake = Pin(gpio.SDD3, Pin.IN)
mcu.mp3_initial()

msg_json = {}

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
    mcu.mqtt_put_msg(topic='Ray', msg=json.dumps(msg_json))

    if distance <= 5:
        mcu.servo_angle(sg_pin, 180)
        time.sleep(2)
    else:
        mcu.servo_angle(sg_pin, 90)

    if earthquake.value() == 1:
        mcu.mp3_start()
        time.sleep(3)  # 填寫音樂秒數
    else:
        mcu.mp3_stop()

    time.sleep(1)