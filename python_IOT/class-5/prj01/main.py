from time import sleep
from machine import Pin, ADC, PWM
from mcu_def import gpio
import time

f = 1000
d = 0
RED = PWM(Pin(gpio.D5), freq=f, duty=d)
GREEN = PWM(Pin(gpio.D6), freq=f, duty=d)
BLUE = PWM(Pin(gpio.D7), freq=f, duty=d)

adc = ADC(0)

while True:
    value = adc.read()
    print(f'value={value}, {round(value*100/1024)}%')
    # sleep(1)

    if (int(value) > 450):  #dark value ~= 1023
        GREEN.duty(0)
        RED.duty(value)
        BLUE.duty(value)
    else:
        GREEN.duty(value)
        RED.duty(value)
        BLUE.duty(value)
