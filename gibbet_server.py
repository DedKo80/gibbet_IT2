# gibbet_server
import random
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode()

        print('Клиент собрался поиграть', self.data)
        x = random.randint(1, 100)

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print('Сервер запущен')
    server.serve_forever()