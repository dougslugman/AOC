import sys
total = 0
points = []
nodes = []
map = []
table = []
start = ''
end = ''

def display(map):
    for i in range(len(map)):
        print(map[i])

def getpoints(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != '#':
                points.append([i, j])

def getdest(map):
    start = ''
    end = ''
    for i in range(len(map)):
        for j in range(len(map[i])):
            if start != '' and end != '':
                return start, end
            if map[i][j] == 'S':
                start = [i, j]
                continue
            elif map[i][j] == 'E':
                end = [i, j]
    if start == '' or end == '':
        print("start and or end was not found") 
        exit()
    else:
        return start, end

def getnodes(map, points):
    global total
    for point in points:
        upord = [point[0] - 1, point[1]]
        downord = [point[0] + 1, point[1]]
        leftord = [point[0], point[1] - 1]
        rightord = [point[0], point[1] + 1]

        upsym = map[upord[0]][upord[1]]
        downsym = map[downord[0]][downord[1]]
        leftsym = map[leftord[0]][leftord[1]]
        rightsym = map[rightord[0]][rightord[1]]

        if (point == end or point == start):
            if((upsym != '#' or downsym != '#') and (leftsym != '#' or rightsym != '#')) == False:
                total = total - 1000
            nodes.append(point)
            continue
        if((upsym != '#' or downsym != '#') and (leftsym != '#' or rightsym != '#')):
            nodes.append(point)

def getdir(map, node, nodes):
    connect = []

    #checkup
    count = 0
    cord = [node[0] -1, node[1]]
    while map[cord[0]][cord[1]] != '#':
        count += 1
        if cord in nodes:
            connect.append([cord, count])
        cord = [cord[0] -1 , cord[1]]
    
    #checkdown
    count = 0
    cord = [node[0] +1, node[1]]
    while map[cord[0]][cord[1]] != '#':
        count += 1
        if cord in nodes:
            connect.append([cord, count])
        cord = [cord[0] +1 , cord[1]]

    #checkleft
    count = 0
    cord = [node[0], node[1] - 1]
    while map[cord[0]][cord[1]] != '#':
        count += 1
        if cord in nodes:
            connect.append([cord, count])
        cord = [cord[0], cord[1] - 1]

    #checkright
    count = 0
    cord = [node[0], node[1] + 1]
    while map[cord[0]][cord[1]] != '#':
        count += 1
        if cord in nodes:
            connect.append([cord, count])
        cord = [cord[0], cord[1] + 1]

    return connect

def settable(table, map, nodes):
    table = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]
    for index, node in enumerate(nodes):
        connection = getdir(map, node, nodes)
        for i in range(len(connection)):
            connecte = nodes.index(connection[i][0])
            table[index][connecte] = connection[i][1] + 1000
            table[connecte][index] = connection[i][1] + 1000
    return table

def dijkstra():
    global total

    startind = nodes.index(start)
    endind = nodes.index(end)


    shortest = [sys.maxsize for _ in range(len(nodes))]
    shortest[startind] = 0  

    
    visited = [False for _ in range(len(nodes))]  
    prev = [None for _ in range(len(nodes))]
    dup = 0
    
    for _ in range(len(nodes)):
        unexplored = [(i, shortest[i]) for i in range(len(nodes)) if not visited[i]]
        node = min(unexplored, key=lambda x: x[1])[0]

        for index, edge in enumerate(table[node]):
            if edge > 0 and visited[index] == False:
                if shortest[node] + edge < shortest[index]:
                    shortest[index] = shortest[node] + edge
                    prev[index] = node
        
        visited[node] = True
    total += shortest[endind]
    path = []
    current = endind
    while current != None:
        path.insert(0, nodes[current])
        current = prev[current]


with open("Text.txt", "r") as file:
    for line in file:
        map.append(list(line.strip()))
start, end = getdest(map)
getpoints(map)
getnodes(map, points)
table = settable(table, map, nodes)
dijkstra()
print(total)