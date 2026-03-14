left = []
right = []
total = 0
with open ("Text.txt", "r") as file:
    for row in file:
        line = row.replace("\n", "")
        line = line.split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))
left.sort()
right.sort()
for i in range(len(left)):
    total += abs(left[i] - right[i])
print(total)