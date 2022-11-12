import time
from time import time

import network
from esp8266_i2c_lcd import I2cLcd
from machine import I2C, PWM, Pin
from umqtt.simple import MQTTClient


class gpio:
    D0 = 16
    D1 = 5
    D2 = 4
    D3 = 0
    D4 = 2
    D5 = 14
    D6 = 12
    D7 = 13
    D8 = 15
    SDD3 = 10
    SDD2 = 9


class mcu_fun:

    def _init_(self):
        self.ip = None
        self.mqClient = None
        self.red = Pin(gpio.D5, Pin.OUT)
        self.green = Pin(gpio.D6, Pin.OUT)
        self.blue = Pin(gpio.D7, Pin.OUT)

    def connect_ap(self, ssid, pwd):
        wlan = network.WLAN(network.STA_IF)
        ap = network.WLAN(network.AP_IF)
        ap.active(False)
        wlan.active(True)
        wlan.scan()
        wlan.connect(ssid, pwd)
        while not (wlan.isconnected()):
            pass
        print('network config:', wlan.ifconfig())
        self.ip = wlan.ifconfig()[0]

    def lcd_initial(self, scl_pin, sda_pin):
        i2c = I2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=400000)
        lcd = I2cLcd(i2c, 0x3F, 2, 16)
        return lcd

    def led_initial(self, r_pin, g_pin, b_pin, mode: str = 'digital'):
        if mode.lower() == 'digital':
            RED = Pin(r_pin, Pin.OUT)
            GREEN = Pin(g_pin, Pin.OUT)
            BLUE = Pin(b_pin, Pin.OUT)
            RED.value(0)
            GREEN.value(0)
            BLUE.value(0)
        else:
            f = 1000
            d = 0
            RED = PWM(Pin(r_pin), freq=f, duty=d)
            GREEN = PWM(Pin(g_pin), freq=f, duty=d)
            BLUE = PWM(Pin(b_pin), freq=f, duty=d)
        return (RED, GREEN, BLUE)

    def connect_mqtt(self, mq_id: str):
        mq_server = "singularmakers.asuscomm.com"
        mq_user = "singular"
        mq_pass = "1234"
        self.mqClient = MQTTClient(mq_id,
                                   mq_server,
                                   user=mq_user,
                                   password=mq_pass,
                                   keepalive=30)
        try:
            self.mqClient.connect()
        except Exception as e:
            print(e)
            sys.exit()
        finally:
            print("connected MQTT server")

    def check_msg(self):
        self.mqClient.check_msg()

    def ping(self):
        self.mqClient.ping()

    def subscribe(self, topic_name: str, on_message):
        self.mqClient.set_callback(on_message)
        self.mqClient.subscribe(topic_name)