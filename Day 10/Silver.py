total = 0
table = []
starting = []
with open("Text.txt", "r") as file:
  for line in file:
    line = list(line.strip())
    table.append(line)
for i in range(len(table)):
  for j in range(len(table[i])):
    if table[i][j] == '0':
      starting.append([i , j])
def search(x, y, searchnum):
  global total, enders
  if searchnum == 9:
    if (x-1) < 0 or (x-1) > (len(table) - 1):
      pass
    else:
      if int(table[x-1][y]) == searchnum and [x-1, y] not in enders:
        enders.append([x-1, y])
        total += 1
    if (x+1) < 0 or (x+1) > (len(table) - 1):
      pass
    else:
      if int(table[x+1][y]) == searchnum and [x+1, y] not in enders:
        enders.append([x+1, y])
        total += 1
    if (y-1) < 0 or (y-1) > (len(table) - 1):
      pass
    else:
      if int(table[x][y-1]) == searchnum and [x, y-1] not in enders:
        enders.append([x, y-1])
        total += 1
    if (y+1) < 0 or (y+1) > (len(table) - 1):
      pass
    else:
      if int(table[x][y+1]) == searchnum and [x, y+1] not in enders:
        enders.append([x, y+1])
        total += 1
  else:
    if (x-1) < 0 or (x-1) > (len(table) - 1):
      pass
    else:
      if int(table[x-1][y]) == searchnum:
        search(x-1, y, searchnum + 1)
    if (x+1) < 0 or (x+1) > (len(table) - 1):
      pass
    else:
      if int(table[x+1][y]) == searchnum:
        search(x+1, y, searchnum + 1)
    if (y+1) < 0 or (y+1) > (len(table) - 1):
      pass
    else:
      if int(table[x][y+1]) == searchnum:
        search(x, y+1, searchnum + 1)
    if (y-1) < 0 or (y-1) > (len(table) - 1):
      pass
    else:
      if int(table[x][y-1]) == searchnum:
        search(x, y-1, searchnum + 1)
for start in starting:
  enders = []
  search(start[0], start[1], 1)
print(total)