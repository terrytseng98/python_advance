import network
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)  #指定 I2C 介面之 GPIO 與傳輸速率
lcd = I2cLcd(i2c, 0x3F, 2, 16)  #指定 I2C Slave 設備位址與顯示器之列數, 行數
wlSSID = "SingularClass0"
wlPWM = "Singular#1234"
wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
ap.active(False)
wlan.active(True)
wlan.scan()
wlan.connect(wlSSID, wlPWM)

while not (wlan.isconnected()):
    pass

lcd.putstr(f"{wlan.ifconfig()[0]}")  #顯示字串
