table = []
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
total = 0

with open("Text.txt", "r") as file:
    for line in file:
        line = list(line)
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

condition = True
currentdir = 0
position = []
for element in start:
    position.append(element)

onmap = True
while onmap == True:
    if (position[0] < 0 or position[1] < 0) or (position[0] > len(table) or position[1] > len(table[0])):
        onmap = False
        continue
    else:
        position[0]+= directions[currentdir][0]
        position[1]+= directions[currentdir][1]
        character = table[position[0]][position[1]]
    if character == '#':
        position[0]-= directions[currentdir][0]
        position[1]-= directions[currentdir][1]
        currentdir+= 1 
        currentdir = currentdir % len(directions)
    table[position[0]][position[1]] = 'X'

for i in range(len(table)):
    for j in range(len(table[i])):
      if table[i][j] == 'X':
        total +=1
        
print(total)