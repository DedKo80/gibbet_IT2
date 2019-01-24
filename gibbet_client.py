# gibbet_client

import socket

HOST = 'localhost'
PORT = 9999

print('Клиент запущен')
print('Подключаемся к серверу {}:{}'.format(HOST, PORT))

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
except:
    print('Ошибка подключения к серверу {}:{}'.format(HOST, PORT))
    sock.close()

try:
    sock.sendall(bytes('START', 'utf-8'))
    receved = sock.recv(1024).decode()
    print(receved)
except:
    pass

