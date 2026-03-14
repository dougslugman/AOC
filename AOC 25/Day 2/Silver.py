ranges = []
total = 0
with open("Text.txt", "r") as file:
    for line in file: ranges = line.strip().split(",")
for window in ranges:
    window = window.split("-")
    for i in range(int(window[0]), int(window[1]) + 1):
        id = str(i)
        if len(id) % 2 != 0:continue
        if id[:len(id)//2] == id[len(id)//2:]: total += int(id)    
print(total)