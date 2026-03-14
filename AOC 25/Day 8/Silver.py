import math
coordinates = []
shortest = []
pairnum = 1000
with open("Text.txt", "r") as file:
    for line in file:
        coordinates.append([int(x) for x in line.strip().split(",")])
def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2) + ((z1 - z2)**2))
lengths = [[999999999999999 for x in range(len(coordinates))] for x in range(len(coordinates))]
for i in range(len(coordinates)):
    for j in range(0, i+1):
        if i==j:
            continue
        dist = distance(coordinates[i][0], coordinates[i][1], coordinates[i][2], coordinates[j][0], coordinates[j][1], coordinates[j][2]) 
        lengths[i][j] = dist
        lengths[j][i] = dist
flattened = []
for i in range(len(coordinates)):
    for j in range(0, i+1):
        flattened.append([lengths[i][j], i, j])
flattened.sort(key=lambda x:x[0])
for x in range(pairnum):
    shortest.append([flattened[x][1], flattened[x][2]])
for i, cord in enumerate(coordinates):
    for j, item in enumerate(cord):
        coordinates[i][j] = str(coordinates[i][j])
sets = []
for i, item in enumerate(coordinates):
    string = ','.join(item)
    sets.append(set())
    sets[i].add(string)
for item in shortest:
    sets[item[0]].update(sets[item[1]])
    for connection in sets[item[1]]:
        sets[coordinates.index(connection.split(","))] = sets[item[0]]
newarr = []
for item in sets:
    if item in newarr:
        continue
    newarr.append(item)
circuits = [len(x) for x in newarr]
circuits.sort(reverse=True)
print(math.prod([circuits[x] for x in range(3)]))