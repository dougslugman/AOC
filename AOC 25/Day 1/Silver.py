current = 50
total = 0
with open ("Text.txt", "r") as f:
    for line in f:
        line = line.strip()
        number = int(line[1:])
        if line[0] == "L":
            current -= number
        else:
            current += number 
        if current % 100 == 0:
            total += 1
print(total)
