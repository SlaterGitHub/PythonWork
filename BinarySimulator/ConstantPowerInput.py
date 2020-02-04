class CPI:
    def __init__(self, node):
        self.power = True
        self.connection = [node]
        if node is not None:
            node.setInput(self.power)

    def setConnection(self, node):
        self.connection.append(node)
        node.setInput(self.power)

    def deleteConnection(self, node):
        if node in self.connection:
            del connection[node]
        node.setInput(False)
        
