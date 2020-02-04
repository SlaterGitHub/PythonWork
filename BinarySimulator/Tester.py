from Transistor import Transistor
from ConstantPowerInput import CPI
from LED import LED

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

def constantPowerTest():
    power = CPI()

    node1 = Transistor(True)

    power.setConnection(node1)

    print(node1.getOutput())
    node1.setSignal(True)
    print(node1.getOutput())
    power.deleteConnection(node1)
    print(node1.getOutput())

def LEDTest():
    power = CPI()

    node1 = Transistor(True)

    led = LED()

    power.setConnection(node1)

    node1.setConnection(led)

    node1.setSignal(True)
    print(led.display())
    node1.setSignal(False)
    print(led.display())

LEDTest()
