from hcsr04 import HCSR04
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
sensor = HCSR04(trigger_pin=gpio.SDD2, echo_pin=(gpio.SDD2))


def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    if msg == "light_on":
        RED.value(1)
        BLUE.value(1)
        GREEN.value(1)
    if msg == "light_off":
        RED.value(0)
        BLUE.value(0)
        GREEN.value(0)
    if msg == "gate_on":
        mcu.servo_angle(sg_pin, 0)
    if msg == "gate_off":
        mcu.servo_angle(sg_pin, 80)

        time.sleep(1)


mcu.mqtt_subscribe(mq_id="Terry", callback=on_message)

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    light = adc.read()
    distance = sensor.distance_cm()
    msg_json["Humidity"] = hum
    msg_json["Temperature"] = temp
    msg_json["light_sensor"] = light
    msg_json["Distance"] = distance
    msg_json["Gate"] = "off"
    if distance <= 5:
        msg_json["Gate"] = "on"
        mcu.servo_angle(sg_pin, 0)
        mcu.mqtt_put_msg(topic="Terry", msg=json.dumps(msg_json))
        time.sleep(3)
        mcu.servo_angle(sg_pin, 80)
    mcu.mqtt_put_msg(topic="Terry", msg=json.dumps(msg_json))
    mcu.mqtt_get_msg(topic="Terry")
    time.sleep(1)