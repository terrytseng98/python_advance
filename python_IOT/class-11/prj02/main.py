from machine import Pin, PWM
from mcu_def import gpio, mcu_fun
import time

mcu = mcu_fun()

sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)
mcu.servo_angle(sg_pin, 0)
time.sleep(1)
mcu.servo_angle(sg_pin, 90)
time.sleep(1)
mcu.servo_angle(sg_pin, 180)
time.sleep(1)
