from time import time
from mcu_def import gpio, mcu_fun
import time
from machine import ADC

adc = ADC(0)
mcu = mcu_fun()
mcu.mqtt_subscribe(mq_id="Terry")

while True:
    value = str(adc.read())
    mcu.mqtt_put_msg("Terry", value)
    time.sleep(1)