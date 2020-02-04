from Bit import Bit

class Pin:
    def __init__(self):
        self.status = Bit(False)

    def setStatus(self, bit):
        self.status.setBit(bit)
        return self.status

    def getStatus(self):
        return self.status.getBit()
