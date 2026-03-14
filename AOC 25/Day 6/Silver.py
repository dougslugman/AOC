import math
total = 0
lines = []
symbols = []
with open("Text.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line[0] == '*':
            line = line.split(" ")
            symbols = line
            break
        line = line.split(" ")
        lines.append(line)
for index, line in enumerate(lines):
    lines[index] = [int(x) for x in line if x != '']
symbols = [x for x in symbols if x != '']
add = False
for vert in range(len(lines[0])):
    vertical = []
    for hoz in range(len(lines)):
        vertical.append(lines[hoz][vert])
    if symbols[vert] == '+':
        total += sum(vertical)
    else:
        total += math.prod(vertical)
print(total)