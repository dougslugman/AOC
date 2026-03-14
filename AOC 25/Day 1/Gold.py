current = 50
total = 0
with open ("Text.txt", "r") as f:
    for index, line in enumerate(f):
        line = line.strip()
        number = int(line[1:])
        if line[0] == "L":
            for _ in range(number):
                current -= 1
                if current < 0:
                    current = 99
                elif current == 0:
                    total += 1
        else:
            for _ in range(number):
                current += 1
                if current > 99:
                    total += 1
                    current = 0
print(total)
