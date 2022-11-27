from machine import Pin
from mcu_def import gpio, mcu_fun
import dht
import time

mcu = mcu_fun()
mcu.connect_ap("SingularClass0", "Singular#1234")
d = dht.DHT11(Pin(gpio.D0, Pin.IN))
mcu.mqtt_subscribe(mq_id="Terry")
lcd = mcu.lcd_initial(scl_pin=gpio.D1, sda_pin=gpio.D2)

while True:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    mcu.mqtt_put_msg(
        topic="Terry",
        msg=f"Humidity:{hum:02d}, Temperature:{temp:02d}{'\u00b0'}c")
    lcd.clear()
    lcd.putstr(f"Humidity:{hum:02d}")
    lcd.move_to(0, 1)  #移到游標至第二列第一行位置 (跳行)
    lcd.putstr(f"Temperature:{temp:02d}{'\u00b0'}c")
    time.sleep(1)