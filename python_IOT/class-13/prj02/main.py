from machine import UART
from time import sleep

uart = UART(1, baudrate=9600)
uart.init(9600, bits=8, parity=None, stop=1)

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
while True:
    buf = bytearray(6)
    buf[0] = 0xAA
    buf[1] = 0x7
    buf[2] = 0x2
    buf[3] = 0x0
    buf[4] = 0x49
    buf[5] = buf[0] + buf[1] + buf[2] + buf[3] + buf[4]
    uart.write(buf)
    sleep(20)