import math
total = 0
lines = []
symbols = []
sizes = []
with open("Text2.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line[0] == '*':
            line = line.split(" ")
            symbols = line
            break
        lines.append(line)
spaces = 1
count = 1
while count < len(symbols):
    symbol = symbols[count]
    if symbol != '':
        sizes.append(spaces)
        spaces = 1
    else: spaces+=1
    count+=1
symbols = [x for x in symbols if x != '' and x != 'x']
start = 0
for index, size in enumerate(sizes):
    large = []
    for x in range(size-1, -1, -1):
        arr = []
        for row in range(len(lines)):
           arr.append(lines[row][x+start])
        arr = int(''.join([x for x in arr if x != " "]))
        large.append(arr)
    start+= size + 1
    if symbols[index] == "+": total += sum(large)
    else: total += math.prod(large)
print(total)