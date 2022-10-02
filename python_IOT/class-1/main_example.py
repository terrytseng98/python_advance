from ast import While
from machine import Pin, PWM
import time

led = Pin(2, Pin.OUT)
led.value(0)
time.sleep(0.1)
led.value(1)
time.sleep(0.1)
led.value(0)
time.sleep(0.1)
led.value(1)
time.sleep(0.1)
f = 1000
d = 0
p2 = PWM(Pin(2), freq=f, duty=d)
for i in range(1024):
    p2.duty(i)
    time.sleep(0.005)
for i in range(1024, -1, -1):
    p2.duty(i)
    time.sleep(0.005)