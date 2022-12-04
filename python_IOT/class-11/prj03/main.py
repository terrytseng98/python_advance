from machine import Pin, ADC, PWM
from mcu_def import gpio, mcu_fun
import dht
import time
import json

mcu = mcu_fun()
adc = ADC(0)
RED, GREEN, BLUE = mcu.led_initial(r_pin=gpio.D5, g_pin=gpio.D6, b_pin=gpio.D7)
mcu.connect_ap("SingularClass0", "Singular#1234")
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
mcu.mqtt_subscribe(mq_id="Terry")
lcd = mcu.lcd_initial(scl_pin=gpio.D1, sda_pin=gpio.D2)
msg_json = {}
sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)


def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    if msg == "on":
        RED.value(1)
        BLUE.value(1)
        GREEN.value(1)
    if msg == "off":
        RED.value(0)
        BLUE.value(0)
        GREEN.value(0)

    try:
        msg = int(msg)
    except:
        pass
    else:
        mcu.servo_angle(sg_pin, msg)
        lcd.clear()
        lcd.putstr(f"Degree:{msg}")
        time.sleep(1)


mcu.mqtt_subscribe(mq_id="Terry", callback=on_message)

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    sensor = adc.read()
    mcu.mqtt_put_msg(topic="Terry", msg=json.dumps(msg_json))
    msg_json["Humidity"] = hum
    msg_json["Temperature"] = temp
    msg_json["light_sensor"] = sensor
    mcu.mqtt_put_msg(topic='Terry', msg=json.dumps(msg_json))
    mcu.mqtt_get_msg(topic="Terry")
    time.sleep(1)