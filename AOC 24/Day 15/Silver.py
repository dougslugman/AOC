total = 0
table = []
moves = ""
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def display(table):
    for row in table:
        print(''.join(row))
    print("\n")
with open("Text1.txt", "r") as file:
    for line in file:
        if line == "\n":
            break
        table.append(list(line.strip()))
    for line in file:
        moves += line.strip()
for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] == '@':
            start = [i, j]
try:
    start = start
except NameError:
    print("No robot found within map")
    exit()
def setboxes(direction, start):
    origin = start[:]
    counter = -1
    while True:
        start = [start[0] + direction[0], start[1] + direction[1]]
        counter += 1
        startchar = table[start[0]][start[1]]
        if startchar == '#':
            return False
        if startchar == '.':
            break
    boxes = []
    for _ in range(counter):
        start = [start[0] - direction[0], start[1] - direction[1]]
        boxes.append(start)
    for box in boxes:
        table[box[0]][box[1]] = '.'
        table[box[0] + direction[0]][box[1] + direction[1]] = 'O'
    table[origin[0]][origin[1]] = '.'
    table[origin[0] + direction[0]][origin[1] + direction[1]] = '@'
    return True
for char in moves:
    if char == '^':
        direction = directions[0]
    elif char == 'v':
        direction = directions[1]
    elif char == '<':
        direction = directions[2]
    elif char == '>':
        direction = directions[3]
    else:
        break
    nextcords = [start[0] + direction[0], start[1] + direction[1]]
    nextchar = table[nextcords[0]][nextcords[1]]
    if nextchar == '#':
        continue
    if nextchar == '.':
        table[nextcords[0]][nextcords[1]] = '@'
        table[start[0]][start[1]] = '.'
        start[:] = [nextcords[0], nextcords[1]]
        continue
    if nextchar == 'O':
        push = setboxes(direction, start)
        if push == True:
            del start
            for i in range(len(table)):
                for j in range(len(table[i])):
                    if table[i][j] == '@':
                        start = [i, j]
            try:
                start = start
            except NameError:
                print("No robot found within map")
                exit()
        continue
for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] == 'O':
            total += ((100 * i) + j)
print(total)