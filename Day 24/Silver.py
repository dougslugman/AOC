import re, copy
startvalues = {re.sub(":", "", k) : int(v) for x in open("Text.txt").read().split("\n\n")[0].split("\n") for k, v in [x.strip().split(" ")]}
startgates = [x.split(" ")[:3] + x.split(" ")[4:] for x in open("Text.txt").read().split("\n\n")[1].split("\n")]
gates = copy.deepcopy(startgates)
values = copy.deepcopy(startvalues)
while gates != []:
    for index, gate in enumerate(gates):
        if gate[0] not in values or gate[2] not in values: continue
        if gate[1] == "XOR": answer = values[gate[0]] ^ values[gate[2]]
        elif gate[1] == "OR": answer = values[gate[0]] | values[gate[2]]
        else: answer = values[gate[0]] & values[gate[2]]
        values[gate[3]] = answer
        gates.pop(index)
print(int(''.join([str(x[1]) for x in sorted([[k, v] for k, v in values.items() if k[0] == "z"], key=lambda x: x[0])[::-1]]),2))