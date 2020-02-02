from Bit import Bit
from Byte import Byte
from ByteCoupler import ByteCoupler

def makeBit():
    return Bit(True)

def makeByte(length):
    bits = []
    for x in range(length):
        bits.append(makeBit())
    return Byte(bits)

def bitTest():
    bit = makeBit()

    print(bit.getBit())
    print(bit.invertBit())
    print(bit.getBit())
    print(bit.setBit(True))

def byteTest():

    byte = makeByte(6)

    print(byte.getByte())
    print(byte.invertByte())
    print(byte.invertBit(5))
    print(byte.leftShift())
    print(byte.rightShift())
    print(byte.getBit(7))

def byteCouplerTest():
    coupler = ByteCoupler(makeByte(6), makeByte(3))

    print(coupler.AND())
    print(coupler.OR())
    print(coupler.NOT())



#bitTest()
#byteTest()
#byteCouplerTest()
