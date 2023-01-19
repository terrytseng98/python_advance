import time
from machine import UART
from time import sleep
from machine import Pin
from mcu_def import gpio, mcu_fun
while True:
    uart = UART(1, baudrate=9600)
    uart.init(9600, bits=8, parity=None, stop=1)
    earthquake = Pin(gpio.SDD3, Pin.IN)
    if earthquake.value() == 1:
        #Volume control(13)
        buf1 = bytearray(5)
        buf1[0] = 0xAA
        buf1[1] = 0x13
        buf1[2] = 0x01
        buf1[3] = 0x7F
        buf1[4] = buf1[0] + buf1[1] + buf1[2] + buf1[3]
        uart.write(buf1)
        #Specify song (07)
        #for i in range(0, 100):
        #   x = 0x53
        buf = bytearray(6)
        buf[0] = 0xAA
        buf[1] = 0x7
        buf[2] = 0x2
        buf[3] = 0x0
        buf[4] = 0x49
        buf[5] = buf[0] + buf[1] + buf[2] + buf[3] + buf[4]
        uart.write(buf)
        time.sleep(10)
    else:
        #Volume control(13)
        buf2 = bytearray(5)
        buf2[0] = 170
        buf2[1] = 4
        buf2[2] = 0
        buf2[3] = 174
        uart.write(buf2)
    time.sleep(0.5)