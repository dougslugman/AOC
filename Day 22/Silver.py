buyers = [int(x.strip()) for x in open("Text.txt")]
total = 0
def nextseq(currentnum):
    step1 = ((currentnum) ^ (currentnum * 64)) % 16777216
    step2 = ((step1) ^ (step1 >> 5)) % 16777216
    step3 = ((step2) ^ (step2 * 2048)) % 16777216
    return step3
for buyer in buyers:
    current = buyer
    for _ in range(2000):
        current = nextseq(current)
    total += current
print(total)