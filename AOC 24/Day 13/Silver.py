import math
total = 0
table = []
def getmin(machiene):
    minimum = 0
    buttonAX = int(machiene[0][0])
    buttonAY = int(machiene[0][1])
    buttonBX = int(machiene[1][0])
    buttonBY = int(machiene[1][1])
    destX = int(machiene[2][0])
    destY = int(machiene[2][1]) 
    amountAX = (destX // buttonAX)
    amountBX = (destX // buttonBX)
    combosX = []
    for i in range(0, amountAX + 1):
        for j in range(0, amountBX + 1):
            if (i * buttonAX) + (j * buttonBX) == destX:
                combosX.append([i, j])
    correct = []
    for i in range(len(combosX)):
        if (combosX[i][0] * buttonAY) + (combosX[i][1] * buttonBY) == destY:
            correct.append(combosX[i])

    correct[:] = [((x[0] * 3) + (x[1])) for x in correct]
    if len(correct) != 0:
        minimum = min(correct)
    return minimum
with open("Text.txt", "r") as file:
    count = 1
    chars = "+=,XY"
    for line in file:
        if count == 1 or count == 2:
            line = line.strip().split(" ")
            line.pop(0)
            line.pop(0)
            for char in chars:
                line[0] = line[0].replace(char, "")
            for char in chars:
                line[1] = line[1].replace(char, "")
            count += 1
            table.append(line)
        elif count == 3 :
            line = line.strip().split(" ")
            line.pop(0)
            for char in chars:
                line[0] = line[0].replace(char, "")
            for char in chars:
                line[1] = line[1].replace(char, "")
            table.append(line)
            count += 1
        else:
            count = 1
            buttonmin = getmin(table)
            total += buttonmin
            table = []
    if table:
        buttonmin = getmin(table)
        total += buttonmin
print(total)