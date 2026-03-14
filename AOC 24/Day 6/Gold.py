global table, directions, total, copy
table = []
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
total = 0
copy = []
with open("Text.txt", "r") as file:
    for line in file:
        line = list(line.strip())
        table.append(line)

for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] == '^':
            start = [i, j]
try:
    start = start
except NameError:
    print("No starting position found\n")
    exit(1)
copy = []
def checkloop():
    global total, directions, table, copy
    prev = set() 
    currentdir = 0
    position = list(start)
    onmap = True
    while onmap:
        position[0] += directions[currentdir][0]
        position[1] += directions[currentdir][1]
        if (position[0] < 0 or position[1] < 0) or (position[0] >= len(table) or position[1] >= len(table[0])):
            onmap = False
            continue
        character = copy[position[0]][position[1]]
        if character == '#':
            position[0] -= directions[currentdir][0]
            position[1] -= directions[currentdir][1]
            state = (position[0], position[1], currentdir)
            if state in prev:
                onmap = False 
                total += 1  
                continue
            else:
                prev.add(state)  
            currentdir = (currentdir + 1) % 4
for i in range(len(table)):
    for j in range(len(table[i])):
        copy = [x[:] for x in table]
        copy[i][j] = '#'
        checkloop()
print(total)