import sys
import network
from machine import I2C, PWM, Pin, UART
from esp8266_i2c_lcd import I2cLcd
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
    def __init__(self):
        self.ip = None
        self.mqClient = None  # 可以當作物件裡的全域變數
        self.uart = None

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

    def led_initial(self, r_pin, g_pin, b_Pin, pwm: bool = False):
        if pwm == False:
            RED = Pin(r_pin, Pin.OUT)
            GREEN = Pin(g_pin, Pin.OUT)
            BLUE = Pin(b_Pin, Pin.OUT)
            RED.value(0)
            GREEN.value(0)
            BLUE.value(0)
        else:
            frequency = 1000
            duty_cycle = 0
            RED = PWM(Pin(r_pin), freq=frequency, duty=duty_cycle)
            GREEN = PWM(Pin(g_pin), freq=frequency, duty=duty_cycle)
            BLUE = PWM(Pin(b_Pin), freq=frequency, duty=duty_cycle)
        return (RED, GREEN, BLUE)

    def lcd_initial(self, scl_pin, sda_pin):
        i2c = I2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=400000)
        lcd = I2cLcd(i2c, 0x3f, 2, 16)
        return lcd

    def mqtt_subscribe(self, mq_id: str, callback=None):
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

        self.mqClient.set_callback(callback)

    def mqtt_get_msg(self, topic: str):
        self.mqClient.subscribe(topic)
        self.mqClient.check_msg()
        self.mqClient.ping()

    def mqtt_put_msg(self, topic: str, msg: str):
        topic = topic.encode('utf-8')
        msg = msg.encode('utf-8')
        self.mqClient.publish(topic, msg)

    def servo_angle(self, sg, angle: int):
        if 0 <= angle <= 180:
            sg.duty(int(1023 * (0.5 + angle / 90) / 20))

    def mp3_initial(self):
        self.uart = UART(1, baudrate=9600)
        self.uart.init(9600, bits=8, parity=None, stop=1)

    def mp3_start(self, volume=0x64, song=0x01):
        '''
        volume = 0~127 (default = 100 = 0x64),
        song = 1~16 (default = 1 = 0x01)
        '''
        # Volume control (13)
        # Command: AA 13 01 VOL SM
        buf1 = bytearray(5)
        buf1[0] = 0xAA
        buf1[1] = 0x13
        buf1[2] = 0x01
        buf1[3] = volume
        buf1[4] = buf1[0] + buf1[1] + buf1[2] + buf1[3]
        self.uart.write(buf1)

        # Specify song (07)
        # Command: AA 07 02 filename(Hi) filename(Lw) SM
        buf = bytearray(6)
        buf[0] = 0xAA
        buf[1] = 0x07
        buf[2] = 0x02
        buf[3] = 0x00  # 音樂檔案開頭名稱的16進制
        buf[4] = song  # 音樂檔案結尾名稱的16進制
        buf[5] = buf[0] + buf[1] + buf[2] + buf[3] + buf[4]
        self.uart.write(buf)

    def mp3_stop(self):
        # Stop (04)
        # Command: AA 04 00 AE
        buf2 = bytearray(4)
        buf2[0] = 0xAA
        buf2[1] = 0x04
        buf2[2] = 0x00
        buf2[3] = 0xAE
        self.uart.write(buf2)
