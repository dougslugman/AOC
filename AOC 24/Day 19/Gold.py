import re
towels = []
paterns = []
total = 0
with open("Test.txt", "r") as file:
    for line in file:
        towels = [x.replace(",", "") for x in line.strip().split(" ")]
        break
    for line in file:
        paterns.append(line.strip())

def getcombo(pos, data, patern):
    global total
    if pos == len(patern):
        total += 1
     
    
    for i, tow in enumerate(data):
        if pos in tow:
            getcombo(pos + len(towels[i]), data, patern)
    return

count = 0
for patern in paterns:
    count += 1
    data = []
    for towel in towels:
        value = [m.start() for m in re.finditer(towel, patern)]
        data.append(value)
    getcombo(0, data, patern)

print(total)