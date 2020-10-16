from packets.message_factory import message_factory
from utils.console import Console
from utils.reader import Reader


class Handler(Reader):
    def __init__(self, client, address):
        super().__init__(b'')
        self.client = client
        self.address = address

        self.console = Console('PyBrawl')
        self.client_console = Console('Client')

        self.handle()

    def handle(self):
        while True:
            try:
                data = self.client.recv(7)
                if data:
                    super().__init__(data)

                    packet_id = self.readUShort()
                    packet_length = self.readUInt(3)
                    packet_version = self.readUShort()

                    packet_data = self.receive(packet_length)

                    self.client_console.update_prefix(f'Client - {packet_id}')
                    self.client_console.print(f'Length: {packet_length}')

                    message = message_factory[packet_id]
                    if message:
                        message = message()
                        message.decode(packet_data)
                        message.process()
                        self.client.send(message.buffer)
            except ConnectionResetError:
                self.console.print(f'{self.address[0]}:{self.address[1]} is disconnected!')
                break

    def receive(self, packet_length):
        data = b''
        while len(data) < packet_length:
            data += self.client.recv(packet_length)
        return data
