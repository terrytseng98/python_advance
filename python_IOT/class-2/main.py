from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)  #指定 I2C 介面之 GPIO 與傳輸速率
lcd = I2cLcd(i2c, 0x3F, 2, 16)  #指定 I2C Slave 設備位址與顯示器之列數, 行數
lcd.putstr("Wellcome,Terry!")  #顯示字串
lcd.move_to(0, 1)  #移到游標至第二列第一行位置 (跳行)
lcd.putstr("It's working!")