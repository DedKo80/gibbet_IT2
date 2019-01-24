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
    print('Ошибка отправки данных на сервер {}:{}'.format(HOST, PORT))
    sock.close()

data = receved.split(';')
if data[0] == 'GUESS':
    print('Угадайте число от {} до {}'.format(data[1], data[2]))
    while True:
        x = input('Ваш ответ (для выхода введите q)')
        if x == 'q':
            sock.sendall(bytes('GOODBYE', 'utf-8'))
            break
        try:
            sock.sendall(bytes('TRY;{}'.format(x), 'utf-8'))
            receved = sock.recv(1024).decode()
        except:
            print('Ошибка отправки числа на сервер {}:{}'.format(HOST, PORT))
            break
        data = receved.split(';')
        if data[0] == 'TRUE':
            print('Вы угадали !!!')
            break
        elif data[0] == 'FALSE':
            if data[2] == '<':
                print('Не угадал! Число меньше. Осталось {} попыток'.format(data[1]))
            else:
                print('Не угадал! Число больше. Осталось {} попыток'.format(data[1]))
        elif data[0] == 'FAIL':
            print('Вы проиграли у-ха-ха')
            break
else:
    print('не известаный ответ сервера')

sock.close()


