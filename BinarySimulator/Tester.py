from Transistor import Transistor

def transistorTest():
    node1 = Transistor(True)
    node2 = Transistor(False)

    node1.setInput(True)
    node2.setInput(True)
    node2.setSignal(False)

    #print(node1.getOutput())
    #node1.setSignal(True)
    #print(node1.getOutput())

    #print(node2.getOutput())
    node2.setSignal(True)
    #print(node2.getOutput())

    node1.setConnection(node2)

    node1.setSignal(False)

    print(node1.getOutput())

    print(node2.getOutput())

transistorTest()
