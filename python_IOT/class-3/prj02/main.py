from machine import Pin, PWM
import time
from mcu_def import gpio

f = 1000
d = 0
RED = PWM(Pin(gpio.D5), freq=f, duty=d)
GREEN = PWM(Pin(gpio.D6), freq=f, duty=d)
BLUE = PWM(Pin(gpio.D7), freq=f, duty=d)
while True:
    for d in range(1023, -1, -1):
        RED.duty(d)
        BLUE.duty(1023 - d)
        time.sleep(0.001)
    for d in range(1023, -1, -1):
        BLUE.duty(d)
        GREEN.duty(1023 - d)
        time.sleep(0.001)
    for d in range(1023, -1, -1):
        GREEN.duty(d)
        RED.duty(1023 - d)
        time.sleep(0.001)