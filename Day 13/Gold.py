import math, numpy
total = 0
table = []
def getmin(machiene):
    buttonAX = int(machiene[0][0])
    buttonAY = int(machiene[0][1])
    buttonBX = int(machiene[1][0])
    buttonBY = int(machiene[1][1])
    destX = int(machiene[2][0]) + 10000000000000
    destY = int(machiene[2][1]) + 10000000000000
    try:
        solutions = numpy.linalg.solve([[buttonAX, buttonBX], [buttonAY, buttonBY]], [destX, destY])
    except numpy.linalg.LinAlgError:
        return 0
    solutions = numpy.round(solutions, 4)
    if (solutions[0] > 0 and solutions[1] > 0):
        if (solutions[0].is_integer() and solutions[1].is_integer()):
            return int((solutions[0] * 3)+ (solutions[1]))
        else:
            return 0
    else:
        return 0
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