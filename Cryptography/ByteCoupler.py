from Byte import Byte

class ByteCoupler:

    def __init__(self, firstByte, secondByte):
        self.bytes = [firstByte, secondByte]

    def AND(self):
        byte = []
        for x in range(8):
            byte.append(self.bothHigh(self.bytes[0].getBit(x+1), self.bytes[1].getBit(x+1)))
        return byte

    def bothHigh(self, firstBit, secondBit):
        return ((firstBit == True) and (secondBit == True))

    def OR(self):
        byte = []
        for x in range(8):
            byte.append(self.eitherHigh(self.bytes[0].getBit(x+1), self.bytes[1].getBit(x+1)))
        return byte

    def eitherHigh(self, firstBit, secondBit):
        return ((firstBit == True) or (secondBit == True))

    def XOR(self):
        byte = []
        for x in range(8):
            byte.append(self.oneHigh(self.bytes[0].getBit(x+1), self.bytes[1].getBit(x+1)))

    def oneHigh(self, firstBit, secondBit):
        return (eitherHigh(firstBit, secondBit) and (bothHigh(firstBit, secondBit) == False))

    def EQUIV(self):
        byte.append(self.isEqual(self.bytes[0].getBit(x+1), self.bytes[1].getBit(x+1)))

    def isEqual(self, firstBit, secondBit):
        return (firstBit == secondBit)

    def NOT(self):
        return self.bytes[0].invertByte()
