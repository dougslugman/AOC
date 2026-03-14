import re
towels = []
paterns = []
visited = set(())
total = 0
with open("Text.txt", "r") as file:
    for line in file:
        towels = [x.replace(",", "") for x in line.strip().split(" ")]
        break
    for line in file:
        paterns.append(line.strip())

def getcombo(pos, data, patern):
    if pos in visited:
        return False
    if pos == len(patern):
        return True
     
    
    for i, tow in enumerate(data):
        if pos in tow:
            if getcombo(pos + len(towels[i]), data, patern):
                return True
    visited.add(pos)
    return False

line = []
count = 0
for patern in paterns:
    data = []
    for towel in towels:
        value = [m.start() for m in re.finditer(towel, patern)]
        data.append(value)
    visited.clear()
    check = getcombo(0, data, patern)
    if check:
        line.append(count)
    count += 1
print(line)