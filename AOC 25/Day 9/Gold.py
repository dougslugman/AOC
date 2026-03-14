import copy
cords = []
with open("text.txt", "r") as file:
    for line in file:
        line = line.strip().split(",")
        line = list(map(int, line))
        cords.append(line)

flat = []
for i, start in enumerate(cords):
    for j in range(i):
        end = cords[j]
        size = (abs(start[0]-end[0])+1)*(abs(start[1]-end[1])+1)
        flat.append([size, cords[i][0], cords[i][1], cords[j][0], cords[j][1]])

flat.sort(key = lambda x:x[0], reverse=True)

cordhoz = []
cordvert = []
vertperim = []
hozperim = []
ishoz = True
if cords[0][0] == cords[1][0]:
    ishoz = False
cords.append(cords[0])
for i in range(len(cords) - 1):
    if ishoz:
        cordhoz.append([cords[i+1][0]-cords[i][0], cords[i][0], cords[i][1]])
        if cords[i][0] <  cords[i+1][0]:
            hozperim.append([cords[i][0], cords[i][1], cords[i+1][0], cords[i+1][1]])
        else:
            hozperim.append([cords[i+1][0], cords[i][1], cords[i][0], cords[i+1][1]])
    else:
        cordvert.append([cords[i][1]-cords[i+1][1], cords[i][0], cords[i][1]])
        if cords[i][1] < cords[i+1][1]:
            vertperim.append([cords[i][0], cords[i][1], cords[i+1][0], cords[i+1][1]])
        else:
            vertperim.append([cords[i][0], cords[i+1][1], cords[i+1][0], cords[i][1]])
    ishoz = not ishoz

cordhoz.sort(key=lambda x:x[1])
cordvert.sort(key=lambda x:x[2])

compoundhoz = [[[0,0,0,0] for y in range(len(cordvert)-1)] for x in range(len(cordvert))]
compoundvert = [[[0,0,0,0] for y in range(len(cordvert))] for x in range(len(cordvert) - 1)]

validhoz = [[False for y in range(len(cordvert)-1)] for x in range(len(cordvert))]
validvert = [[False for y in range(len(cordvert))] for x in range(len(cordvert) - 1)]

hozcords = {}
vertcords = {}
hozstart = 0
for i in range(len(cordhoz)-1):
    hozlen = (cordhoz[i+1][1] - cordhoz[i][1]) + 1
    hozstart = cordhoz[i][1]

    for j in range(len(cordvert)-1):
        vertlen = (cordvert[j+1][2] - cordvert[j][2]) + 1
        vertstart = cordvert[j][2]

        hozline = [hozstart, vertstart, hozstart+hozlen-1, vertstart]
        nexthozline = [hozstart, vertstart+vertlen-1 ,hozstart+hozlen-1, vertstart+vertlen-1]
        vertline = [hozstart, vertstart ,hozstart, vertstart+vertlen-1 ]
        nextvertline = [hozstart+hozlen-1, vertstart, hozstart+hozlen-1, vertstart+vertlen-1]

        compoundhoz[j][i] = hozline
        hozcords[','.join([str(x) for x in hozline])] = [j, i]
        hozcords[','.join([str(x) for x in hozline][:2]) + 's'] = [j, i]
        hozcords[','.join([str(x) for x in hozline][2:]) + 'e'] = [j, i]

        compoundhoz[j+1][i] = nexthozline
        hozcords[','.join([str(x) for x in nexthozline])] = [j+1, i]
        hozcords[','.join([str(x) for x in nexthozline][:2]) + 's'] = [j+1, i]
        hozcords[','.join([str(x) for x in nexthozline][2:]) + 'e'] = [j+1, i]

        compoundvert[j][i] = vertline
        vertcords[','.join([str(x) for x in vertline])] = [j, i]
        vertcords[','.join([str(x) for x in vertline][:2]) + 's'] = [j, i]
        vertcords[','.join([str(x) for x in vertline][2:]) + 'e'] = [j, i]

        compoundvert[j][i+1] = nextvertline
        vertcords[','.join([str(x) for x in nextvertline])] = [j, i+1]
        vertcords[','.join([str(x) for x in nextvertline][:2]) + 's'] = [j, i+1]
        vertcords[','.join([str(x) for x in nextvertline][2:]) + 'e'] = [j, i+1]

for i in range(len(compoundhoz[0])):
    isvalid = False
    for j in range(len(compoundhoz)):
        if isvalid:
            validhoz[j][i] = True
        window = compoundhoz[j][i]
        for item in hozperim:
            if window[1] != item[1]:
                continue
            if window[0] >= item[0] and window[2] <= item[2]:
                isvalid = not isvalid
                break
        if isvalid:
            validhoz[j][i] = True

for i in range(len(compoundvert)):
    isvalid = False
    for j in range(len(compoundvert[0])):
        if isvalid:
            validvert[i][j] = True
        window = compoundvert[i][j]
        for item in vertperim:
            if window[0] != item[0]:
                continue
            if window[1] >= item[1] and window[3] <= item[3]:
                isvalid = True
                break
        if isvalid:
            validvert[i][j] = True

for item in flat:
    size = item[0]
    if item[1] == item[3] or item[2] == item[4]:
        continue
    x = [item[1], item[3]]
    y = [item[2], item[4]]
    topleft = [str(min(x)), str(min(y))]
    topright = [str(max(x)), str(min(y))]
    bottomleft = [str(min(x)), str(max(y))]
    bottomright = [str(max(x)), str(max(y))]


    valid = True
    # topleft to topright

    done = False
    single = ','.join(topleft)+ ',' + ','.join(topright)
    if single in hozcords:
        if validhoz[hozcords[single][0]][hozcords[single][1]] == True:
            done = True
    current = copy.deepcopy(hozcords[','.join(topleft)+'s'])
    end = copy.deepcopy(hozcords[','.join(topright)+'e'])
    while valid and not done:
        if validhoz[current[0]][current[1]] == False:
            valid = False
            continue
        if current == end:
            break
        current[1] += 1
    if not valid:
        continue


    # bottomleft to bottomright

    done = False
    single = ','.join(bottomleft)+ ',' + ','.join(bottomright)
    if single in hozcords:
        if validhoz[hozcords[single][0]][hozcords[single][1]] == True:
            done = True
    current = copy.deepcopy(hozcords[','.join(bottomleft)+'s'])
    end = copy.deepcopy(hozcords[','.join(bottomright)+'e'])
    while valid and not done:
        if validhoz[current[0]][current[1]] == False:
            valid = False
            continue
        if current == end:
            break
        current[1] += 1
    if not valid:
        continue


#   topleft to bottomleft

    done = False
    single = ','.join(topleft)+ ',' + ','.join(bottomleft)
    if single in vertcords:
        if validvert[vertcords[single][0]][vertcords[single][1]] == True:
            done = True
    current = copy.deepcopy(vertcords[','.join(topleft)+'s'])
    end = copy.deepcopy(vertcords[','.join(bottomleft)+'e'])
    while valid and not done:
        if validvert[current[0]][current[1]] == False:
            valid = False
            continue
        if current == end:
            break
        current[0] += 1
    if not valid:
        continue


    # topright to bottomright
    
    done = False
    single = ','.join(topright)+ ',' + ','.join(bottomright)
    if single in vertcords:
        if validvert[vertcords[single][0]][vertcords[single][1]] == True:
            done = True
    current = copy.deepcopy(vertcords[','.join(topright)+'s'])
    end = copy.deepcopy(vertcords[','.join(bottomright)+'e'])
    while valid and not done:
        if validvert[current[0]][current[1]] == False:
            valid = False
            continue
        if current == end:
            break
        current[0] += 1
    if not valid:
        continue
    print(item[0])
    break