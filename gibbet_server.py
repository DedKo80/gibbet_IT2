# gibbet_server
import random
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode()


        if self.data == 'START':
            try_count = random.randint(8, 12)
            print('Клиент собрался поиграть', self.data)
            x = random.randint(1, 100)
            print('Загадано число {}'.format(x))
            self.request.sendall(bytes('GUESS;1;100;{}'.format(try_count), 'utf-8'))

            while True:
                self.data = self.request.recv(1024).decode()
                print('клиент ответил: ', self.data)
                resp = self.data.split(';')
                if resp[0] == 'TRY':
                    if int(resp[1]) == x:
                        self.request.sendall(bytes('TRUE', 'utf-8'))
                        print('Клиент выиграл')
                    else:
                        try_count -= 1
                        if try_count == 0:
                            self.request.sendall(bytes('FAIL', 'utf-8'))
                            print('Клиент проиграл')
                            break
                        else:
                            if x < int(resp[1]):
                                self.request.sendall(bytes('FALSE;{};<'.format(try_count), 'utf-8'))
                                print('Загаданное число меньше')
                            else:
                                self.request.sendall(bytes('FALSE;{};>'.format(try_count), 'utf-8'))
                                print('Загаданное число больше')
                elif resp[0] == 'GOODBYE':
                    self.request.sendall(bytes('GOODBYE', 'utf-8'))
                    print('Клиент отключился')
                    break
                else:
                    print('Неизвестный запрос')
                    break



if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print('Сервер запущен')
    server.serve_forever()