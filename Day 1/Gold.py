left = []
right = []
total = 0
with open ("Text.txt", "r") as file:
    for row in file:
        line = row.replace("\n", "")
        line = line.split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))
for i in range(len(left)):
    appearance = 0
    for j in range(len(right)):
        if left[i] == right[j]:
            appearance+=1
    total+= (appearance * left[i])
print(total)
