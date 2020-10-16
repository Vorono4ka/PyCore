import threading
import socket

from handler import Handler


class Server:
    def __init__(self):
        self.socket = socket.socket()

    def start(self, ip=None, port=None):
        if ip is None:
            ip = 'localhost'
        if port is None:
            port = 9339

        self.socket.bind((ip, port))

    def listen(self):
        self.socket.listen()
        while True:
            client, address = self.socket.accept()

            print(f'Connect from {address[0]}:{address[1]}')

            client_thread = threading.Thread(target=Handler, args=(client, address))
            client_thread.start()


if __name__ == '__main__':
    server = Server()
    server.start()
    server.listen()
