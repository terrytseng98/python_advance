from machine import Pin
from time import sleep
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

p2=Pin(2, Pin.OUT)

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)  #指定 I2C 介面之 GPIO 與傳輸速率
lcd = I2cLcd(i2c, 0x3F, 2, 16)  #指定 I2C Slave 設備位址與顯示器之列數, 行數


while True:
    p2.value(0)
    lcd.putstr("on")  #顯示字串
    sleep(1)
    lcd.clear()
    p2.value(1)
    lcd.putstr("off")  #顯示字串
    sleep(1)
    lcd.clear()