table = []
frequencies = []
total = 0
occ = 0
with open("Text.txt", "r") as file:
    for line in file:
        table.append(list(line.strip()))
for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] != '.':
            occ += 1
        if table[i][j] != '.' and table[i][j] not in frequencies:
            frequencies.append(table[i][j])
antinodemap = [x[:] for x in table]
for item in frequencies:
    coordinates = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == item:
                coordinates.append([i, j])
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if coordinates[i] == coordinates[j]:
                continue
            count = 1
            cont = True
            while cont:
                count += 1
                antinode = [coordinates[j][0] - coordinates[i][0], coordinates[j][1] - coordinates[i][1]]
                antinode[0] *= count
                antinode[1] *= count
                antinode[0] += coordinates[i][0]
                antinode[1] += coordinates[i][1]
                if (antinode[0] < 0 or antinode[0] > len(antinodemap) - 1) or (antinode[1] < 0 or antinode[1] > len(antinodemap[0]) - 1):
                    cont = False
                    continue
                if antinodemap[antinode[0]][antinode[1]] != '#' and antinodemap[antinode[0]][antinode[1]] not in frequencies:
                    antinodemap[antinode[0]][antinode[1]] = '#'
                    total += 1
print(total + occ)



