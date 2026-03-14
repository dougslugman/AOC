total = 0
jolts = 12
with open("Text.txt", "r") as file:
    for line in file:
        line = line.strip()
        batteries = [-1 for x in range(jolts)]
        index = -1
        for battery in range(jolts):
            for i in range(index+1, (len(line)-((jolts-1)-battery))):
                if int(line[i]) > batteries[battery]:
                    batteries[battery] = int(line[i])
                    index = i
        total += int(''.join([str(x) for x in batteries]))
print(total)