size = 0
end = 1176
start = 1176
winner = 0
loser = 0
total = 0

rules = []
pages = []
global others
others = []
ranked = []
ordered = []

linecount = 0  
def getind(comp):
    for i in range(len(others)):
        if comp == others[i]:
            return i


def display():
  print(others)
  for i in range(len(ranked)):
    for j in range(len(ranked)):
      print(str(ranked[i][j]))
    print("new line\n\n\n")
    

with open("Text.txt", "r") as file:
  for row in file:
    linecount+=1
    row = row.split("|")
    row[1] = row[1].replace("\n", "")
    rules.append(row)
    if linecount >= end:
      break
    for i in range(len(rules)):
      for j in range(2):
       if rules[i][j] in others:
         continue
       else:
         others.append(rules[i][j])
  size = len(others)
  for i in range(size):
    ranked.append([])
    for j in range(size):
      ranked[i].append(False)
  others.sort()
  for i in range(len(rules)):
    winner = 0
    loser = 0
    for j in range(len(others)):
      if rules[i][0] == others[j]:
        winner = j
    for j in range(len(others)):
      if rules[i][1] == others[j]:
        loser = j
    ranked[winner][loser] = True
    ranked[loser][winner] = False
  for line in file:
      line = line.replace("\n", "")
      line = line.split(",")
      copy = [x for x in line]
      linstr = len(line)
      ordered = []
      for k in range(linstr):
          for i in range(len(line)):
              isloser = True
              for j in range(len(line)):
                 try:
                    if ranked[getind(line[i])][getind(line[j])] == True:
                      isloser = False
                 except IndexError:
                     isloser = False
              if isloser == True:
                  ordered.append(line[i])
                  line.pop(i)
      ordered.reverse()
      if ordered == copy:
         total += int(ordered[len(ordered)//2])
                  
              
  print(total)