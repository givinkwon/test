# Card
class Card:
    def __init__(self):
        self.Number = 0
        self.PIN = 0

    def set(self, value):
        self.Number = value[0]
        self.PIN = value[1]
        return self
