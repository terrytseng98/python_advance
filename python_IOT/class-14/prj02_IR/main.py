from machine import Pin
from mcu_def import gpio
from time import sleep

IR = Pin(gpio.D3, Pin.IN)

while True:
    print(IR.value())
    sleep(1)