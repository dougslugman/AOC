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

  popmap = []
  topdown = [row[:] for row in region]
  for i in range(len(topdown)):
    if topdown[i][0] - 1 < 0:
      continue
    if (table[topdown[i][0] - 1][topdown[i][1]]) == identifier:
      popmap.append(i)
  popmap.reverse()
  for i in range(len(popmap)):
    topdown.pop(popmap[i])
  lines = list({x[0] for x in topdown})
  for line in lines:
    blocks = [x for x in topdown if x[0] == line]
    blocks.sort(key=lambda x:x[1])
    prev = -2
    perimeter += len(blocks)
    for block in blocks:
      if block[1] == prev + 1:
        perimeter -= 1
      prev = block[1]

  popmap = []
  downtop = [row[:] for row in region]
  for i in range(len(downtop)):
    if downtop[i][0] + 1 >= len(table):
      continue
    if (table[downtop[i][0] + 1][downtop[i][1]]) == identifier:
      popmap.append(i)
  popmap.reverse()
  for i in range(len(popmap)):
    downtop.pop(popmap[i])
  lines = list({x[0] for x in downtop})
  for line in lines:
    blocks = [x for x in downtop if x[0] == line]
    blocks.sort(key=lambda x:x[1])
    prev = -2
    perimeter += len(blocks)
    for block in blocks:
      if block[1] == prev + 1:
        perimeter -= 1
      prev = block[1]

  popmap = []
  leftright = [row[:] for row in region]
  for i in range(len(leftright)):
    if leftright[i][1] + 1 >= len(table[0]):
      continue
    if (table[leftright[i][0]][leftright[i][1] + 1]) == identifier:
      popmap.append(i)
  popmap.reverse()
  for i in range(len(popmap)):
    leftright.pop(popmap[i])
  lines = list({x[1] for x in leftright})
  for line in lines:
    blocks = [x for x in leftright if x[1] == line]
    blocks.sort(key=lambda x:x[0])
    prev = -2
    perimeter += len(blocks)
    for block in blocks:
      if block[0] == prev + 1:
        perimeter -= 1
      prev = block[0]

  popmap = []
  rightleft = [row[:] for row in region]
  for i in range(len(rightleft)):
    if rightleft[i][1] - 1 < 0:
      continue
    if (table[rightleft[i][0]][rightleft[i][1] - 1]) == identifier:
      popmap.append(i)
  popmap.reverse()
  for i in range(len(popmap)):
    rightleft.pop(popmap[i])
  lines = list({x[1] for x in rightleft})
  for line in lines:
    blocks = [x for x in rightleft if x[1] == line]
    blocks.sort(key=lambda x:x[0])
    prev = -2
    perimeter += len(blocks)
    for block in blocks:
      if block[0] == prev + 1:
        perimeter -= 1
      prev = block[0]
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