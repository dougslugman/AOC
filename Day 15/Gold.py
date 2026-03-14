total = 0
table = []
moves = ""
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

boxcords = []
boxenders = []

def display(table, char):
    for row in table:
        print(''.join(row))
    print(char)
    print("\n\n")
    
with open("Text2.txt", "r") as file:
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

def lrboxes(direction, start):
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
        table[box[0] + direction[0]][box[1] + direction[1]] = table[box[0]][box[1]]
        table[box[0]][box[1]] = '.'
    table[origin[0]][origin[1]] = '.'
    table[origin[0] + direction[0]][origin[1] + direction[1]] = '@'
    return True

def findboxes(direction, start):
    boxcords.append(start)
    if table[start[0] + direction[0]][start[1] + direction[1]] == '[':
        findboxes(direction, [start[0] + direction[0], start[1] + direction[1]])
        findboxes(direction, [start[0] + direction[0] + directions[3][0], start[1] + direction[1] + directions[3][1]])

    elif table[start[0] + direction[0]][start[1] + direction[1]] == ']':
        findboxes(direction, [start[0] + direction[0], start[1] + direction[1]])
        findboxes(direction, [start[0] + direction[0] + directions[2][0], start[1] + direction[1] + directions[2][1]])

    else:
        boxenders.append([start[0] + direction[0], start[1] + direction[1]])
        return 

def udboxes(direction, start):
    global boxenders, boxcords
    origin = start[:]
    boxcords.clear()
    boxenders.clear()

    findboxes(direction, start)

    boxcords.pop(0)
    boxcords = list(map(list, set(map(tuple, boxcords))))
    boxenders = list(map(list, set(map(tuple, boxenders))))

    for end in boxenders:
        if table[end[0]][end[1]] != '.':
            return False
        
    if direction == [1, 0]:
        boxcords.sort(key=lambda x: x[0])
        boxcords.reverse()
    else:
        boxcords.sort(key=lambda x: x[0])

    for part in boxcords:
        table[part[0] + direction[0]][part[1] + direction[1]] = table[part[0]][part[1]]
        table[part[0]][part[1]] = '.'
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
        table[start[0]][start[1]] = '.'
        table[start[0] + direction[0]][ start[1] + direction[1]] = '@'
        start[:] = [nextcords[0], nextcords[1]]
        continue

    if direction == directions[0] or direction == directions[1]:
        push = udboxes(direction, start)
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

    else:
        push = lrboxes(direction, start)
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
        if table[i][j] == '[':
          total += ((100 * i) + j) 
print(total)