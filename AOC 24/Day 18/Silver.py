import sys
values = []
plane = []
byte = 1024
start = [0, 0]
def display(table):
    for row in table:
        print(''.join(row))
with open("Text.txt", "r") as file:
    for line in file:
        line = [int(x) for x in (line.strip().split(","))]
        line.reverse()
        values.append(line)
for i in range(71):
    plane.append(["." for x in range(71)])
for index, cord in enumerate(values):
    if index >= byte:
        break
    plane[cord[0]][cord[1]] = '#'
dots = []
for i in range(len(plane)):
    for j in range(len(plane[i])):
        if plane[i][j] == '.':
            dots.append([i, j])
tree = []
end = [70,70]
for dot in dots:
    nearby = []
    if (dot[0] - 1) < 0:
        pass
    else:
        if plane[dot[0] - 1][dot[1]] == '.':
            nearby.append([dot[0] - 1, dot[1]])
    if (dot[0] + 1) >= len(plane):
        pass
    else:
        if plane[dot[0] + 1][dot[1]] == '.':
            nearby.append([dot[0] + 1, dot[1]])
    if (dot[1] - 1) < 0:
        pass
    else:
        if plane[dot[0]][dot[1] - 1] == '.':
            nearby.append([dot[0], dot[1] - 1])
    if (dot[1] + 1) >= len(plane[0]):
        pass
    else:
        if plane[dot[0]][dot[1] + 1] == '.':
            nearby.append([dot[0], dot[1] + 1])
    tree.append(nearby)
    
visited = [False for _ in range(len(dots))]
length = [sys.maxsize for x in range(len(dots))]
length[dots.index(start)] = 0
near = tree[dots.index(start)]
for _ in range(len(dots)):
    unexplored = [[index, x] for index, x in enumerate(length) if visited[index] == False]
    unexplored.sort(key=lambda x:x[1])
    node = unexplored[0][0]
    for index, edge in enumerate(tree[node]):
        if length[node] + 1 < length[dots.index(edge)]:
            length[dots.index(edge)] = length[node] + 1
    visited[node] = True

print(length[dots.index(end)])