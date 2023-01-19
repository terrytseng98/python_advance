from machine import Pin
from mcu_def import mcu_fun
from mcu_def import gpio
from time import sleep

IR = Pin(gpio.D3, Pin.IN)
mcu = mcu_fun()
mcu.mp3_initial()

while True:
    print(IR.value())
    if IR.value() == 1:
        mcu.mp3_start(song=0x02)
        sleep(3)
    else:
        mcu.mp3_stop()
    sleep(1)