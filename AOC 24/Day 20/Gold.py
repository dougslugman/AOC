total = 0
CardinalRange = 20
start = None
end = None
dots = []
cache = []
table = [list(x.strip()) for x in open("Text.txt")]
c = len(table[0])
r = len(table)

def display(table):
    for row in table:
        print(''.join(row))

def getcardinal(table, point):
    cheatends = []
    for x in range(1, CardinalRange + 1):
        for y in range((CardinalRange + 1) - x):
            if x + point[0] >= (r) or y + point[1] >= (c):
                continue
            if table[x + point[0]][ y + point[1]] == '#':
                continue
            if x+y <= 1:
                continue
            cheatends.append([x + point[0], y + point[1], x+y])


    for x in range(-(CardinalRange + 1), 0):
        for y in range(-((CardinalRange) + x), 1):
            if x + point[0] < 0 or y + point[1] < 0:
                continue
            if table[x + point[0]][ y + point[1]] == '#':
                continue
            if abs(x + y) <= 1:
              continue
            cheatends.append([x + point[0], y + point[1], abs(x + y)])


    for x in range(-(CardinalRange + 1), 1):
        for y in range(1, (CardinalRange + 1) + x):
            if x + point[0] < 0 or y + point[1] >= (c):
                continue
            if table[x + point[0]][ y + point[1]] == '#':
                continue
            if abs(x)+y <= 1:
                continue
            cheatends.append([x + point[0], y + point[1], abs(x)+y])
    
    for x in range(0, CardinalRange + 1):
        for y in range(-(CardinalRange - x), 0):
            if x + point[0] >= (r) or y + point[1] < 0:
                continue
            if table[x + point[0]][ y + point[1]] == '#':
                continue
            if x+abs(y) <= 1:
                continue
            cheatends.append([x + point[0], y + point[1], x+abs(y)])
    
    return cheatends

for i, column in enumerate(table):
    for j, row in enumerate(column):
        if start is not None and end is not None:
            break
        if row == 'E':
            end = (i, j)
        elif row == 'S':
            start = (i, j)
    else:
        continue
    break

if start is None or end is None:
    print("end or start position wasnt found")
    exit(0)

prev = None
current = start[:]
while True:
    dots.append(current)
    if table[current[0] + 1][current[1]] == '.' and (current[0] + 1, current[1]) != prev:
        prev = current
        current = (current[0] + 1, current[1])
        continue

    elif table[current[0] - 1][current[1]] == '.' and (current[0] - 1, current[1]) != prev:
        prev = current
        current = (current[0] - 1, current[1])
        continue

    elif table[current[0]][current[1] + 1] == '.' and (current[0], current[1] + 1) != prev:
        prev = current
        current = (current[0], current[1] + 1)
        continue

    elif table[current[0]][current[1] - 1] == '.' and (current[0], current[1] - 1) != prev:
        prev = current
        current = (current[0], current[1] - 1)
        continue
    dots.append(end)
    break

for _ in range(r):
    cache.append([None for x in range(c)])

for pos, dot in enumerate(dots):
    cache[dot[0]][dot[1]] = len(dots) - (pos + 1)

done = set()
dup = 0
total = 0
for dot in dots:
    cheatends = getcardinal(table, dot)
    for end in cheatends:
        if (dot[0],dot[1],end[0],end[1]) in done:
            continue
        done.add((end[0],end[1],dot[0],dot[1]))
        if(cache[dot[0]][dot[1]] - cache[end[0]][end[1]] - end[2]) >= 100:
            total += 1

print(total)