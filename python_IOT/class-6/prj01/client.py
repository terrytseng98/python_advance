import socket

s = socket.socket()
s.connect(('127.0.0.1', 25536))
while True:
    msg = input('Input Message:')
    s.send(msg.encode('utf8'))
    reply = s.recv(128).decode('utf8')
    if reply == 'quit':
        print('Disconnected')
        s.close()
        break
    print(reply)
