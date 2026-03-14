'''
IMPORTANT, this code will not print out the output, you need to manualy look through the text file it reads to to find a christmas tree
Change the start and end values that you want to search, btoh start and end are inclusive to being outputed into the text file
'''

total = 0
table = []
copy = []
BOUNDX = 101
BOUNDY = 103
start = 7371
end = 7371
rm = ["p", "=", "v"]
open('Output.txt', 'w').close()

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

for k in range(start, end+1):
    print(f"Iteration {k} written to file!")
    table = []
    copy = []
    for i in range(BOUNDX):
        copy.append([' ' for x in range(BOUNDY)])
    with open("Text.txt", "r") as file:
        for line in file:
            line = line.strip().split(" ")
            line[0] = ''.join([x for x in line[0] if x not in rm])
            line[1] = ''.join([x for x in line[1] if x not in rm])
            line[0] = line[0].split(",")
            line[1] = line[1].split(",")
            position = getpos(line, k)
            copy[position[0]][position[1]] = '#'
    for i in range(len(copy[0])):
        table.append([])
        for j in range(len(copy)):
            table[i].append(copy[j][i])

    with open("Output.txt", "a") as file:
        file.writelines(str(k))
        for i in range(len(table)):
            file.writelines(str(table[i]))
            file.writelines("\n")
        file.writelines("\n")

