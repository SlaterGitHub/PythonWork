class Bit:
    def __init__(self, bit):
        self.bit = bit

    def getBit(self):
        return self.bit

    def setBit(self, bit):
        self.bit = bit
        return self.bit

    def invertBit(self):
        self.bit = not self.bit
        return self.bit
