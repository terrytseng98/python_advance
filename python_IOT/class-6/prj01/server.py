from http import client
import socket

HOST = 'localhost'  #IP
PORT = 25536
s = socket.socket()
s.bind((HOST, PORT))
s.listen(5)  #伺服器端最多可接受多少
print('server:{} port:{} start'.format(HOST, PORT))
client, addr = s.accept()  #伺服器端接收並回傳對象與IP位置資訊
print('client address:{}, port:{}'.format(addr[0], addr[1]))
while True:
    msg = client.recv(100).decode('utf8')
    print('Receive Message:' + msg)

    if msg == 'Hi':
        client.send(b'Hello!')
    elif msg == 'Bye':
        client.send(b'quit')
        break
    else:
        client.send(b'what?')

client.close()  #關閉與客戶端溝通
s.close()  #關閉伺服器
