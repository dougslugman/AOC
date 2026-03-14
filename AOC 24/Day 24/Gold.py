FILE = "solved.txt"
import re
import copy
from functools import cache
def display(table):
    for i, l in enumerate(table):
        print(i, l)
    print("\n")
startvalues = {re.sub(":", "", k) : int(v) for x in open(FILE).read().split("\n\n")[0].split("\n") for k, v in [x.strip().split(" ")]}
startgates = [x.split(" ")[:3] + x.split(" ")[4:] for x in open(FILE).read().split("\n\n")[1].split("\n")]
gates = copy.deepcopy(startgates)
values = copy.deepcopy(startvalues)


display(gates)
badbits = []

def getxor1(index, gate, x, y):
    if (gate[0] == x and gate[2] == y and gate[1] == "XOR"): return index, gate[3]
    if (gate[2] == x and gate[0] == y and gate[1] == "XOR"): return index, gate[3]
    return False, False

def getand1(index, gate, x, y):
    if (gate[0] == x and gate[2] == y and gate[1] == "AND"): return index, gate[3]
    if (gate[2] == x and gate[0] == y and gate[1] == "AND"): return index, gate[3]
    return False, False

def getxor2(index, gate, num1, z):
    if (gate[3] == z and gate[1] == "XOR"):
        if (gate[0] == num1): return index, gate[2]
        if (gate[2] == num1): return index, gate[0]
    return False, False
    
def getand2(index, gate, num1, num3):
    if ((gate[0] == num1 and gate[2] == num3) or (gate[0] == num3 and gate[2] == num1)) and gate[1] == "AND": return index, gate[3]
    return False, False


def getor1(index, gate, num2, num4):
    if (gate[0] == num2 and gate[2] == num4) or (gate[0] == num4 and gate[2] == num2) and gate[1] == "OR": return index, gate[3]
    return False, False


def addercheck(num):
    x, y, z = "x" + num, "y" + num, "z" + num
    xor1, xor2, and1, and2, or1, num1, num2, num3, num4, num5 = None, None, None, None, None, None, None, None, None, None


    for index, gate in enumerate(gates):
        xor1, num1 = getxor1(index, gate, x, y)
        if xor1 != False:
            break
    else:
        return "XOR1 FALSE"
    

    for index, gate in enumerate(gates):
        and1, num2 = getand1(index, gate, x, y)
        if and1 != False:
            break
    else:
        return "AND1 FALSE"
    

    for index, gate in enumerate(gates):
        xor2, num3 = getxor2(index, gate, num1, z)
        if xor2 is not False:
            break
    else:
        return "XOR2 FALSE"
    

    for index, gate in enumerate(gates):
        and2, num4 = getand2(index, gate, num1, num3)
        if and2 != False:
            break
    else:
        return "AND2 FALSE"   
    

    for index, gate in enumerate(gates):
        or1, num5 = getor1(index, gate, num2, num4)
        if or1 != False:
            break
    else:
        return "OR1 FALSE"
    
    return "GOOD"

for i in range(1, 45):
    i = str(i)
    if len(i) < 2:
        i = i.zfill(2)
    print(addercheck(i), i)