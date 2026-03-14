from functools import cache
total = 0
starting = [x.strip() for x in open("Text.txt", "r").readline().split(" ")]
@cache
def lower(val, depth, limit): 
  if depth == limit: return 1
  if val == "0": stones = ["1"]
  elif len(val) % 2 == 0: stones = [str(int(val[:len(val)//2])), str(int(val[len(val)//2:]))]
  else: stones = [str(int(val) * 2024)]
  sum = 0
  for stone in stones: sum += lower(stone, depth+1, limit)
  return sum 
for start in starting: total += lower(start, 0, 75)
print(total)