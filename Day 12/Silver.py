total = 0
table = []
taken = []
region = []
with open("Text.txt", "r") as file:
  for line in file:
    table.append(list(line.strip()))


def getregion(identifier, start):
  global region, table
  
  if start[0]+ 1 < len(table):
    if table[start[0] + 1][start[1]] == identifier and [start[0] + 1, start[1]] not in region:
      region.append([start[0] + 1, start[1]])
      getregion(identifier , [start[0] + 1, start[1]])

  if start[0] - 1 >= 0:
    if table[start[0] - 1][start[1]] == identifier and [start[0] - 1, start[1]] not in region:
      region.append([start[0] - 1, start[1]])
      getregion(identifier , [start[0] - 1, start[1]])
  
  if start[1] + 1 < len(table[0]):
    if table[start[0]][start[1] + 1] == identifier and [start[0], start[1] + 1] not in region:
      region.append([start[0], start[1] + 1])
      getregion(identifier , [start[0], start[1] + 1])
      
  if start[1] - 1 >= 0:
    if table[start[0]][start[1] - 1] == identifier and [start[0], start[1] - 1] not in region:
      region.append([start[0], start[1] - 1])
      getregion(identifier , [start[0], start[1] - 1])


def getper(identifier):
  global table, region
  perimeter = 0
  
  for i in range(len(region)):
    
    
    if region[i][0] + 1 >= len(table):
      perimeter += 1
    else:
      if table[region[i][0] + 1][region[i][1]] != identifier:
        perimeter += 1
        
        
    if region[i][0] - 1 < 0:
      perimeter += 1
    else:
      if table[region[i][0] - 1][region[i][1]] != identifier:
        perimeter += 1
        
        
    if region[i][1] + 1 >= len(table[0]):
      perimeter += 1
    else:
      if table[region[i][0]][region[i][1] + 1] != identifier:
        perimeter += 1
        
    
    if region[i][1] - 1 < 0:
      perimeter += 1
    else:
      if table[region[i][0]][region[i][1] - 1] != identifier:
        perimeter += 1
  return perimeter
        
for i in range(len(table)):
  for j in range(len(table[i])):
    if [i, j] not in taken:
      region.append([i, j])
      getregion(table[i][j], [i, j])
      taken.extend(region)
      area = len(region)
      perimeter = getper(table[i][j])
      total += (perimeter * area)
      region.clear()
      
print(total)