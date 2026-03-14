table = []
total = 0
x = "XMAS"
def display(x, y):
    print(f"i = {x}, j = {y}")
with open("Text.txt", "r") as file:
    for line in file:
        line = list(line.strip())
        table.append(line)
for i in range(len(table)):
    for j in range(len(table[i])):
        if j + 3 < len(table[i]):  # Check right
            chunk = table[i][j] + table[i][j+1] + table[i][j+2] + table[i][j+3]
            if chunk == x:
                total += 1
        if j - 3 >= 0:  # Check left
            chunk = table[i][j] + table[i][j-1] + table[i][j-2] + table[i][j-3]
            if chunk == x:
                total += 1
        if i - 3 >= 0:  # Check up
            chunk = table[i][j] + table[i-1][j] + table[i-2][j] + table[i-3][j]
            if chunk == x:
                total += 1
        if i + 3 < len(table):  # Check down
            chunk = table[i][j] + table[i+1][j] + table[i+2][j] + table[i+3][j]
            if chunk == x:
                total += 1
        if i - 3 >= 0 and j - 3 >= 0:  # Diagonal TL
            chunk = table[i][j] + table[i-1][j-1] + table[i-2][j-2] + table[i-3][j-3]
            if chunk == x:
                total += 1
        if i - 3 >= 0 and j + 3 < len(table[i]):  # Diagonal TR
            chunk = table[i][j] + table[i-1][j+1] + table[i-2][j+2] + table[i-3][j+3]
            if chunk == x:
                total += 1
        if i + 3 < len(table) and j - 3 >= 0:  # Diagonal BL
            chunk = table[i][j] + table[i+1][j-1] + table[i+2][j-2] + table[i+3][j-3]
            if chunk == x:
                total += 1
        if i + 3 < len(table) and j + 3 < len(table[i]):  # Diagonal BR
            chunk = table[i][j] + table[i+1][j+1] + table[i+2][j+2] + table[i+3][j+3]
            if chunk == x:
                total += 1
print(total)