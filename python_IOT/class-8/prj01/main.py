from time import time
from umqtt.simple import MQTTClient
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
from mcu_def import gpio, mcu_fun
import time

mcu = mcu_fun()
mcu.connect_ap("SingularClass0", "Singular#1234")
mcu.connect_mqtt(mq_id="Terry")
RED, GREEN, BLUE = mcu.led_initial(r_pin=gpio.D5, g_pin=gpio.D6, b_pin=gpio.D7)

lcd = mcu.lcd_initial(scl_pin=gpio.D1, sda_pin=gpio.D2)

#RED = mcu_fun().red
#GREEN = mcu_fun().green
#BLUE = mcu_fun().blue

RED.value(0)
BLUE.value(0)
GREEN.value(0)

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)  #指定 I2C 介面之 GPIO 與傳輸速率
lcd = I2cLcd(i2c, 0x3F, 2, 16)  #指定 I2C Slave 設備位址與顯示器之列數, 行數
wlan = mcu_fun()
wlan.connect_ap("SingularClass0", "Singular#1234")

mq_server = "singularmakers.asuscomm.com"
mq_id = "Terry"
mq_user = "singular"
mq_pass = "1234"
mqClient0 = MQTTClient(mq_id,
                       mq_server,
                       user=mq_user,
                       password=mq_pass,
                       keepalive=30)
try:
    mqClient0.connect()
except Exception as e:
    print(e)
    exit()
finally:
    print("connected MQTT server")


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


mqClient0.set_callback(on_message)
mqClient0.subscribe("Terry")

while True:
    mqClient0.check_msg()
    mqClient0.ping()
    time.sleep(0.1)