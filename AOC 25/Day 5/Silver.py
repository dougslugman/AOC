windows = []
total = 0
checking = False
with open("Text.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not checking:
            if line == "@":
                checking = True
                continue
            windows.append(list(map(int, line.split("-"))))
        else:
            line = int(line)
            for window in windows:
                if line >= window[0] and line <= window[1]:
                    total+=1
                    break
print(total)