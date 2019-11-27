def readDecimals(decs, bins):
    decimalLines = decs.readlines()
    varName = ""
    fullBinary = ""
    halfBinaries = ["",""]

    for line in decimalLines:
        splitLine = line.split()
        fullBinary = "{0:b}".format(int(splitLine[2]))
        if(len(fullBinary) < 8):
            halfBinaries[0] = completeEightBit(fullBinary)
            halfBinaries[1] = "00000000"
        else:
            print(fullBinary)
            halfBinaries[0] = fullBinary[-8:]
            fullBinary = fullBinary[:-8]
            halfBinaries[1] = completeEightBit(fullBinary)
        bins.write(splitLine[0]+"L = "+halfBinaries[0]+"\n")
        bins.write(splitLine[0]+"H = "+halfBinaries[1]+"\n")

def completeEightBit(bits):
    loops = 8 - len(bits)
    for x in range(loops):
        bits = "0" + bits
    return bits

decimals = open("D:\\ProgrammingLanguages\\Python\\PythonWork\\binaryConversion\\decimals.txt", "r")
binaries = open("D:\\ProgrammingLanguages\\Python\\PythonWork\\binaryConversion\\binaries.txt", "a+")

readDecimals(decimals, binaries)
decimals.close()
binaries.close()
