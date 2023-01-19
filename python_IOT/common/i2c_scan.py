from machine import I2C, Pin
from mcu_def import gpio

i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:', len(devices))

    for device in devices:
        print("Decimal address: ", device, " | Hexa address: ", hex(device))
