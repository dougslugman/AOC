total = 0
grid = []
with open("Text.txt", "r") as file:
    for line in file:
        grid.append([x for x in line.strip()])
removed = True
while removed:
    removed=False
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            count = 0
            if char != '@':
                continue
            if i-1 > -1 and j-1 > -1:
                if grid[i-1][j-1] != '.':
                    count += 1
            if i-1 > -1:
                if grid[i-1][j] != '.':
                    count += 1
            if i-1 > -1 and j+1 < len(line):
                if grid[i-1][j+1] != '.':
                    count += 1
            if j-1 > -1:
                if grid[i][j-1] != '.':
                    count += 1
            if j+1 < len(line):
                if grid[i][j+1] != '.':
                    count+=1
            if i+1 < len(grid) and j-1 > -1:
                if grid[i+1][j-1] != '.':
                    count += 1
            if i+1 < len(grid):
                if grid[i+1][j] != '.':
                    count += 1
            if i+1 < len(grid) and j+1 < len(line):
                if grid[i+1][j+1] != '.':
                    count += 1
            if count < 4:
                grid[i][j] = "x"
                removed=True  
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "x":
                grid[i][j] = '.'
                total += 1
print(total)