import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    client.subscribe("Terry")


def on_message(client, userdata, msg):
    print(f"我訂閱的主題是:{msg.topic}, 收到訊息:{msg.payload.decode('utf-8')}")


client = mqtt.Client()
client.on_connect = on_connect  # 設定連線的動作
client.on_message = on_message  # 設定接收訊息的動作
client.username_pw_set("singular", "1234")  # 設定登入帳號密碼
client.connect("singularmakers.asuscomm.com", 1883, 60)
#設定連線資訊(IP,Port,連線時間)
#開始連線，執行設定的動作和處理重新連線問題
#也可以手動使用其他1oop函式來進行連接
client.loop_forever()