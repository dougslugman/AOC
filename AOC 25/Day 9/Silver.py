cords = []
with open("Text.txt", "r") as file:
    for line in file:
        line = line.strip().split(",")
        line = list(map(int, line))
        cords.append(line)
flat = []
for i, start in enumerate(cords):
    for j in range(i):
        end = cords[j]
        size = (abs(start[0]-end[0])+1)*(abs(start[1]-end[1])+1)
        flat.append([size, i, j])
print(max(flat, key=lambda x:x[0])[0])
