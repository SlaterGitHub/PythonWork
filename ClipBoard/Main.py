import tkinter

class textFile():
    def __init__(self, filePath):
        self.PATH = "D:\\ProgrammingLanguages\\Python\\PythonWork\\ClipBoard\\"
        self.file = self.PATH + filePath

    def readFull(self):
        openedFile = open(self.file, "r")
        content = openedFile.read()
        openedFile.close()
        return content

    def readLine(self):
        openedFile = open(self.file, "r")
        content = openedFile.readlines()
        openedFile.close()
        return content

    def writeLine(self, content):
        openedFile = open(self.file, "a")
        openedFile.write(content)
        openedFile.close()

    def splitBy(self, divider):
        content = self.readFull()
        chars = ""
        entries = []
        starter = divider[0]
        x = 0

        while(x < len(content)):
            if content[x] == starter:
                if self.divCheck(divider, content[x:x+3]):
                    entries.append(chars)
                    chars = ""
                    x+=3
            chars += content[x]
            x+=1

        return entries

    def divCheck(self, divider, text):
        if divider == text:
            return True
        return False
