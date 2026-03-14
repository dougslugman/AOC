import functools
grid = []
with open("Text.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = [x for x in line]
        grid.append(line)
start = f"0,{''.join(grid[0]).find("S")}"
@functools.cache
def split(coordinate):
    coordinate = coordinate.split(",")
    i = int(coordinate[0])
    j = int(coordinate[1])
    total = 0
    while True:
        symbol = grid[i][j]
        if symbol == "^":
            total += split(f"{i},{j+1}")
            total += split(f"{i},{j-1}")
            break
        if symbol == "x": 
            total += 1
            break
        i += 1
    return total
print(split(start))