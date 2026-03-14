grid = []
global total
total = 0
with open("Text.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = [x for x in line]
        grid.append(line)
start = []
for i,row in enumerate(grid):
    for j,char in enumerate(row):
        if char == "S":
            start = [i, j]
def split(coordinate):
    global total
    while True:
        if  grid[coordinate[0]][coordinate[1]] == "¦": return
        if grid[coordinate[0]][coordinate[1]] == "^":
            total += 1
            grid[coordinate[0]][coordinate[1]] = "O"
            split([coordinate[0], coordinate[1] + 1])
            split([coordinate[0], coordinate[1] - 1])
            return
        if grid[coordinate[0]][coordinate[1]] == "x": return
        grid[coordinate[0]][coordinate[1]] = "¦"
        coordinate = [coordinate[0] + 1, coordinate[1]] 
split(start)
print(total)