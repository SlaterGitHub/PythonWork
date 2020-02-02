binaries = open("D:\\ProgrammingLanguages\\Python\\PythonWork\\binaryConversion\\binaries.txt", "r")
tableBinaries = open("D:\\ProgrammingLanguages\\Python\\PythonWork\\binaryConversion\\binariesTables.txt", "a+")
segmentBinaries = open("D:\\ProgrammingLanguages\\Python\\PythonWork\\binaryConversion\\sevenSegmentBinary.txt", "r")
segmentTable = open("D:\\ProgrammingLanguages\\Python\\PythonWork\\binaryConversion\\SevenSegmentTables.txt", "a+")

def readBinaries(binaries, table):
    table.write("\nHBits: \n.db ")
    bits = binaries.readlines()
    for bit in  bits:
        bit = bit.split()
        if(bit[0][1] == "H"):
            table.write("0b"+bit[2]+", ")

def readSegments(binaries, table):
    table.write("SegmentBits: \n db. ")
    bits = binaries.readlines()
    for bit in bits:
        bit = bit.split()
        table.write("0b"+bit[2]+", ")

readSegments(segmentBinaries, segmentTable)
segmentTable.close()
