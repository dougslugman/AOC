buyers = [int(x.strip()) for x in open("Text.txt")]
prices = []
seqtoprice = []
seen = set()
def nextseq(currentnum):
    step1 = ((currentnum) ^ (currentnum * 64)) % 16777216
    step2 = ((step1) ^ (step1 >> 5)) % 16777216
    step3 = ((step2) ^ (step2 * 2048)) % 16777216
    return step3
for buyer in buyers:
    current = buyer
    prices.clear()
    seen.clear()
    seqtoprice.append({})
    for index in range(2000):
        prices.append(current % 10)
        current = nextseq(current)
        if index > 3:
            difference = ','.join([str(prices[x] - prices[x-1]) for x in range(1, 5)])
            prices.pop(0)
            if difference not in seen:
                seqtoprice[-1][difference] = prices[-1]
                seen.add(difference)
seqsum = {}   
for index, buyer in enumerate(seqtoprice):
    for k, v in buyer.items():
        if k in seqsum:
            seqsum[k] += v
        else:
            seqsum[k] = v
print(max(seqsum.values()))