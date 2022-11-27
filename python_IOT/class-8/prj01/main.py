from time import time
from umqtt.simple import MQTTClient
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
from mcu_def import gpio, mcu_fun
import time

mcu = mcu_fun()
mcu.connect_ap("SingularClass0", "Singular#1234")

RED, GREEN, BLUE = mcu.led_initial(r_pin=gpio.D5, g_pin=gpio.D6, b_pin=gpio.D7)

lcd = mcu.lcd_initial(scl_pin=gpio.D1, sda_pin=gpio.D2)


def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    lcd.clear()
    lcd.putstr(f"topic:{topic}")
    lcd.move_to(0, 1)  #移到游標至第二列第一行位置 (跳行)
    lcd.putstr(f"msg:{msg}")
    if msg == "on":
        RED.value(1)
        BLUE.value(1)
        GREEN.value(1)
    if msg == "off":
        RED.value(0)
        BLUE.value(0)
        GREEN.value(0)


mcu.mqtt_subscribe(mq_id="Terry", callback=on_message)

while True:
    mcu.mqtt_get_msg(topic="Terry")
    time.sleep(0.1)