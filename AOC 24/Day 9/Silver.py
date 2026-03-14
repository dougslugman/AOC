total = 0
unordered = []
count = -1
dots = []
numbers = []
with open("Text.txt", "r") as file:
    for line in file:
        for i in range(len(line)):
            if i % 2 == 0:
                count += 1
                for j in range(int(line[i])):
                    unordered.append(int(count))
            else:
                for j in range(int(line[i])):
                    unordered.append('.')
for i in range(len(unordered)):
    if isinstance(unordered[i], int):
        numbers.append(i)
for i in range(len(numbers)):
    if unordered[i] == '.':
        dots.append(i)
numbers.reverse()
for i in range(len(dots)):
    unordered[dots[i]] = unordered[numbers[i]]
    unordered[numbers[i]] = '.'
for i in range(len(unordered)):
    if unordered[i] == '.':
        break
    total += unordered[i] * i
print(total)