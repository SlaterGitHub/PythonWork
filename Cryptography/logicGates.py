from ByteCoupler import ByteCoupler

def makeCoupler(primary, secondary):
    return ByteCoupler(primary, secondary)

def AND(primary, secondary):
    return makeCoupler(primary, secondary).AND()

def OR(primary, secondary):
    return makeCoupler(primary, secondary).OR()

def NOT(primary, secondary):
    return makeCoupler(primary, secondary).NOT()

def EQUIV(primary, secondary):
    return makeCoupler(primary, secondary).EQUIV()

def XOR(primary, secondary):
    return makeCoupler(primary, secondary).XOR()
