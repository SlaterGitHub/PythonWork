class CPI:
    power = True

    def __init__(self, *args):
        if len(args) == 1:
            self.connection = [args[0]]
            self.connection.setInput(self.power)
        else:
            self.connection = []

    def setConnection(self, node):
        self.connection.append(node)
        node.setInput(self.power)

    def deleteConnection(self, node):
        if node in self.connection:
            self.connection.remove(node)
        node.setInput(not self.power)
