import copy, itertools
from functools import cache
total = 0
numeric = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
directional = [[None, "^", "A"], ["<", "v", ">"]]
codes = ["A" + x.strip() for x in open("Text.txt")]

numvals = {}
for i, c in enumerate(numeric):
    for j, val in enumerate(c):
        if val == None:
            continue
        numvals[val] = str(i) + str(j)
dirvals = {}
for i, c in enumerate(directional):
    for j, val in enumerate(c):
        if val == None:
            continue
        dirvals[val] = str(i) + str(j)


def getconnections(graph):
    r = len(graph)
    c = len(graph[0])
    connections = [[[] for _ in range(len(x))] for x in graph]
    for i, row in enumerate(graph):
        for j, val in enumerate(row):
            if i-1 >= 0:
                if graph[i-1][j] != None and val != None:
                    connections[i][j].append(str(i-1)+str(j) + "^")
            
            if i+1 < r:
                if graph[i+1][j] != None and val != None:
                    connections[i][j].append(str(i+1)+str(j) + "v")

            if j-1 >= 0:
                if graph[i][j-1] != None and val != None:
                    connections[i][j].append(str(i)+str(j-1) + "<")
            
            if j+1 < c:
                if graph[i][j+1] != None and val != None:
                    connections[i][j].append(str(i)+str(j+1) + ">")
    return connections
def BFS(graph, scr, dst):
    if scr == dst:
        return ["A"]
    queue = []
    queue.append([scr[0] + scr[1], "", [[False for _ in range(len(x))] for x in graph]])
    queue[0][2][int(scr[0])][int(scr[1])] = True
    connections = getconnections(graph)
    optimalen = float("inf")
    optimals =[]
    while queue != []:
        current = queue[0]
        for connection in connections[int(current[0][0])][int(current[0][1])]:
            if len(current[1]) + 1 > optimalen:
                break
            if connection[:2] == dst:
                if len(current[1]) + 1 < optimalen:
                    optimalen = len(current[1]) + 1
                    optimals.append(current[1] + connection[2:] + "A")
                elif len(current[1]) + 1 == optimalen:
                    optimals.append(current[1] + connection[2:] + "A")
            else:
                if current[2][int(connection[0])][int(connection[1])] == True:
                    continue
                else:
                    queue.append([connection[:2], current[1] + connection[2:], current[2]])
                    queue[-1] = copy.deepcopy(queue[-1])
                    queue[-1][2][int(connection[0])][int(connection[1])] = True
        else:
            queue.pop(0)
            continue
        break
    return optimals


numtable = {}
for i1, x1 in enumerate(numeric):
    for j1, y1 in enumerate(x1):
        if numeric[i1][j1] == None:
            continue
        for i2, x2 in enumerate(numeric):
            for j2, y2 in enumerate(x2):
                if numeric[i2][j2] == None:
                    continue
                numtable[str(i1)+str(j1)+str(i2)+str(j2)] = BFS(numeric, str(i1)+str(j1), str(i2)+str(j2))
dirtable = {}
for i1, x1 in enumerate(directional):
    for j1, y1 in enumerate(x1):
        if directional[i1][j1] == None:
            continue
        for i2, x2 in enumerate(directional):
            for j2, y2 in enumerate(x2):
                if directional[i2][j2] == None:
                    continue
                dirtable[str(i1)+str(j1)+str(i2)+str(j2)] = BFS(directional, str(i1)+str(j1), str(i2)+str(j2))

def real(seq):
    parts = []
    for index in range(1, len(seq)):
        c1 = numvals[seq[index - 1]]
        c2 = numvals[seq[index]]
        part = (numtable[c1+c2])
        parts.append(part)
    cartisian = [''.join(element) for element in itertools.product(*parts)]
    return cartisian

optimallen = {k:len(v[0]) for k,v in dirtable.items()}

@cache
def proxy(vals, depth, limit):
    if depth == limit:
        return optimallen[vals]
    
    optimals = dirtable[vals]
    sequencelen = 0

    shortest = float("inf")
    for section in optimals:
        section = "A" + section
        sequencelen = 0
        for index in range(1, len(section)):
            sequencelen += proxy(dirvals[section[index - 1]] + dirvals[section[index]], depth+1, limit)
        if sequencelen < shortest:
            shortest = sequencelen
    return shortest

for code in codes:
    dir1 = real(code)
    minimum = float("inf")
    for direction in dir1:
        direction = "A" + direction
        l = 0
        for index in range(1, len(direction)):
            l+=proxy(dirvals[direction[index - 1]]+dirvals[direction[index]], 0, 24)
        if l < minimum:
            minimum = l
    total += minimum * int(code[1:-1])

print(total)