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
for k, v in nearby.items(): 
    for other1 in v:
        for other2 in v:
            if "t"!= k[0] and "t" != other1[0] and "t" != other2[0]: continue
            if other2 in nearby[other1] and other1 in nearby[other2]: total += 0.5
print(int(total/3))