# Dear reader, this code is terribly written but only because I challenged myself to write it in under 10 lines, I promise I write better code than this
total, keys, locks = 0, [], []
for index, block in enumerate(open("Text.txt").read().split("\n\n")):
    block = [list(x) for x in [l for l in block.split("\n")]]
    if all([True if x == "#" else False for x in block[0]]): locks.append(tuple([len([True for x in [block[j][i] for j in range(len(block))] if x =="#"]) - 1 for i in range(len(block[0]))]))
    else: keys.append(tuple([len([True for x in [block[j][i] for j in range(len(block))] if x =="#"]) - 1 for i in range(len(block[0]))]))
for lock in locks:
    for key in keys:
        if all([True if e < 6 else False for e in[x+y for x, y in zip(lock, key)]]): total += 1
print(total)