table = []
total = 0
with open("Text.txt", "r") as file:
    for line in file:
        line = list(line.strip())
        table.append(line)
for i in range(1, len(table) - 1):
    for j in range(1, len(table[i]) - 1):  
        if table[i][j] == 'A':
            leftup = table[i-1][j-1] + table[i][j] + table[i+1][j+1]
            rightup = table[i-1][j+1] + table[i][j] + table[i+1][j-1]
            if (leftup == "MAS" or leftup == "SAM") and (rightup == "MAS" or rightup == "SAM"):
                total += 1
print(total)
