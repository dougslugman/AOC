total = 0
table = []
copy = []
BOUNDX = 101
BOUNDY = 103
rm = ["p", "=", "v"]

for i in range(BOUNDX):
    copy.append([0 for x in range(BOUNDY)])

def getpos(line, time):
    posx = int(line[0][0])
    posy = int(line[0][1])
    volx = int(line[1][0])
    voly = int(line[1][1])
    movement = [time*volx, time*voly]
    movement[0] += posx
    movement[1] += posy
    movement[0] = movement[0] % (BOUNDX)
    movement[1] = movement[1] % (BOUNDY)
    return movement



with open("Text.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")
        line[0] = ''.join([x for x in line[0] if x not in rm])
        line[1] = ''.join([x for x in line[1] if x not in rm])
        line[0] = line[0].split(",")
        line[1] = line[1].split(",")
        position = getpos(line, 100)
        copy[position[0]][position[1]] += 1


for i in range(len(copy[0])):
    table.append([])
    for j in range(len(copy)):
        table[i].append(copy[j][i])

quad = 0
for i in range(len(table)//2):
    for j in range(len(table[0])//2):
        quad += table[i][j]
total += quad


quad = 0
for i in range((len(table)//2) + 1, BOUNDY):
    for j in range(len(table[0])//2):
        quad += table[i][j]
total *= quad


quad = 0
for i in range((len(table)//2) + 1, BOUNDY):
    for j in range((len(table[0])//2) + 1 ,BOUNDX):
        quad += table[i][j]
total *= quad


quad = 0
for i in range((len(table)//2)):
    for j in range((len(table[0])//2) + 1 ,BOUNDX):
        quad += table[i][j]
total *= quad
print(total)



