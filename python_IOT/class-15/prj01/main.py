from hcsr04 import HCSR04
from machine import Pin, ADC, PWM
from mcu_def import gpio, mcu_fun
import dht
import time
import json

mcu = mcu_fun()
mcu.connect_ap("SingularClass0", "Singular#1234")
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
# type: ignoremcu.mqtt_subscribe(mq_id="Terry")
sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)
msg_json = {}


def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(msg)
    if msg == "Me":
        mcu.servo_angle(sg_pin, 0)
        time.sleep(3)
        mcu.servo_angle(sg_pin, 80)


mcu.mqtt_subscribe(mq_id="Terry", callback=on_message)
mcu.servo_angle(sg_pin, 80)
while True:
    mcu.mqtt_get_msg(topic="Terry_AI")
    time.sleep(1)