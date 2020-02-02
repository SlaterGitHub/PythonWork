from Byte import Byte

class ByteCoupler:

    def __init__(self, firstByte, secondByte):
        self.bytes = [firstByte, secondByte]

    def AND(self):
        byte = []
        for x in range(8,0,-1):
            byte.append(self.bothHigh(self.bytes[0].getBit(x), self.bytes[1].getBit(x)))
        return byte

    def bothHigh(self, firstBit, secondBit):
        return (firstBit and secondBit)

    def OR(self):
        byte = []
        for x in range(8,0,-1):
            byte.append(self.eitherHigh(self.bytes[0].getBit(x), self.bytes[1].getBit(x)))
        return byte

    def eitherHigh(self, firstBit, secondBit):
        return (firstBit or secondBit)

    def XOR(self):
        byte = []
        for x in range(8,0,-1):
            byte.append(self.oneHigh(self.bytes[0].getBit(x), self.bytes[1].getBit(x)))

        return byte

    def oneHigh(self, firstBit, secondBit):
        return (self.eitherHigh(firstBit, secondBit) and (self.bothHigh(firstBit, secondBit) == False))

    def EQUIV(self):
        byte = []
        for x in range(8,0,-1):
            print(x)
            byte.append(self.isEqual(self.bytes[0].getBit(x), self.bytes[1].getBit(x)))
        return byte

    def isEqual(self, firstBit, secondBit):
        return (firstBit == secondBit)

    def NOT(self):
        return self.bytes[0].invertByte()

    def setByte(byte, index):
        self.bytes[index+1] = byte
