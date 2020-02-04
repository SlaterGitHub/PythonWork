from Pin import Pin

class LED:

    def __init__(self):
        self.state = Pin()
        self.color = "Black"

    def setSignal(self, bit):
        self.state.setStatus(bit)
        return self.display()

    def display(self):
        if(self.state.getStatus()):
            self.color = "White"
        else:
            self.color = "Black"
        return self.color
