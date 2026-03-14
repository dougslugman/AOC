import itertools
total = 0
connections = [x.strip() for x in open("Text.txt")]
nearby = {}
tripples = set()
for connection in connections:
    c1, c2 = connection.split("-")
    if c1 not in nearby: nearby[c1] = set()
    nearby[c1].add(c2)
    if c2 not in nearby: nearby[c2] = set()
    nearby[c2].add(c1)
def allcon(combo):
    for con1 in combo:
        for con2 in combo:
            if con1 == con2:
                continue
            if con2 not in nearby[con1]:
                return False
    return True
for i in range(13, 0, -1):
    for k, v in nearby.items():
        combinations = itertools.combinations(v, i)
        for combo in combinations:
            if allcon(combo) == True:
                best = list(combo)
                best.append(k)
                break
        else:
            continue
        break
    else:
        continue
    break
print(','.join(sorted(best)))