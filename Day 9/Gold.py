total = 0
unordered = []
count = -1
dots = []
numbers = []
def find_index_by_id(target_id, lst):
    for idx, elem in enumerate(lst):
        if id(elem) == target_id:
            return idx
def getdots(position):
    array = []
    for i in range(position):
        if unordered[i][0] == '.':
            array.append(i)
    return array
with open("Text.txt", "r") as file:
    for line in file:
        for i in range(len(line)):
            section = []
            if i % 2 == 0:
                count += 1
                for j in range(int(line[i])):
                    section.append(int(count))
            else:
                for j in range(int(line[i])):
                    section.append('.')
            if section != []:
                unordered.append(section)
for i in range(len(unordered)):
    if isinstance(unordered[i][0], int):
        numbers.append(id(unordered[i]))
numbers.reverse()
for number in numbers:
    value = find_index_by_id(number, unordered)
    dots = getdots(value)
    if dots == []:
        continue
    done = False
    for j in range(len(dots)):
        if done == True:
            break
        dotcount = len(unordered[dots[j]])
        numcount = len(unordered[value]) 
        if dotcount >= numcount:
            for k in range(len(unordered[value])):
                unordered[dots[j]][k] = unordered[value][k]
                value = find_index_by_id(number, unordered)
                unordered[value][k] = '.'
                done = True
        else:
            continue
        dotcount = 0
        for k in range(len(unordered[dots[j]])):
            if unordered[dots[j]][k] == '.':
                dotcount += 1
        unordered[dots[j]] = [x for x in unordered[dots[j]] if x != '.']
        remaining = []
        for k in range(dotcount):
            remaining.append('.')
        if remaining != []:
            unordered.insert(dots[j] + 1, remaining)
unordered = [item for sublist in unordered for item in sublist]
total = sum(int(unordered[i]) * i for i in range(len(unordered)) if unordered[i] != '.')
print(total)