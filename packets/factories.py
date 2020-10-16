class Factory:
    def __init__(self):
        self.initiators = {}

    def add_initiator(self, key, initiator):
        self.initiators[key] = initiator

    def get_initiator(self, key):
        if key in self.initiators:
            return self.initiators[key]
        return None

    def __setitem__(self, key, value):
        self.add_initiator(key, value)

    def __getitem__(self, item):
        return self.get_initiator(item)


class MessageFactory(Factory):
    def add_message(self, key, initiator):
        self.add_initiator(key, initiator)

    def get_message(self, key):
        return self.get_initiator(key)


class CommandFactory(Factory):
    def add_command(self, key, initiator):
        self.add_initiator(key, initiator)

    def get_command(self, key):
        return self.get_initiator(key)
