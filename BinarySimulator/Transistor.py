from Pin import Pin

class Transistor:

    def __init__(self, pud):
        self.pud = pud
        self.pins = {"input" : Pin(), "signal" : Pin(), "output" : Pin()}
        self.connection = None

    def setSignal(self, bit):
        if(self.pud == bit):
            self.pins["output"].setStatus(self.pins["input"].getStatus())
        else:
            self.pins["output"].setStatus(False)

        if self.connection is not None:
            self.connection.setSignal(self.pins["output"].getStatus())
        return self.pins["output"].getStatus()

    def getOutput(self):
        return self.pins["output"].getStatus()

    def setInput(self, bit):
        self.pins["input"].setStatus(bit)
        return self.pins["input"].getStatus()

    def setConnection(self, node):
        self.connection = node
