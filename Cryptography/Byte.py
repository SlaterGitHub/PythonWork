from Bit import Bit

class Byte:

    def __init__(self, bits):
        self.bits = self.formatByte(bits)

    def updateBit(self, bit, index):
        self.bits[8-(index-1)-1] = bit
        return self.getByte()

    def invertBit(self, index):
        self.bits[8-(index-1)-1].invertBit()
        return self.getByte()

    def invertByte(self):
        for bit in self.bits:
            bit.invertBit()
        return self.getByte()

    def leftShift(self):
        self.bits = self.bits[-7:]
        self.bits.append(Bit(False))
        return self.getByte()

    def rightShift(self):
        tempBits = [Bit(False)]
        for x in range(7):
            tempBits.append(self.bits[x])
        self.bits = tempBits
        return self.getByte()

    def formatByte(self, bits):
        for x in range(8-len(bits)):
            bits.insert(0, Bit(False))
        return bits

    def getBit(self, index):
        return self.bits[8-(index-1)-1].getBit()

    def setBit(self, index, bit):
        self.bits[8-(index-1)-1].setBit(bit)

    def getByte(self):
        byte = []
        for x in range(len(self.bits)):
            byte.append(self.bits[x].getBit())

        return byte
