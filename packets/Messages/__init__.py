from utils.reader import Reader
from utils.writer import Writer


class Message(Writer, Reader):
    def __init__(self):
        super().__init__()
        self.id = 0

    def decode(self, buffer):
        Reader.__init__(self, buffer)

    def encode(self):
        Writer.__init__(self)

    def process(self):
        pass

    def pack(self):
        packet_data = self.buffer
        Writer.__init__(self)
        self.writeShort(self.id)
        self.writeUInt(len(packet_data), 3)
        self.writeShort(0)  # Version
        self.buffer += packet_data + b'\xff\xff\x00\x00\x00\x00\x00'
