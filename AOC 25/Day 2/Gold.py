ranges = []
factors = []
total = 0
length = 0
def calculate(length):
    temp =[]
    for i in range(1, (length//2)+1):
        if length % i == 0:
            temp.append([i, int(length/i)])
    return temp
with open("Text.txt", "r") as file:
    for line in file: ranges = line.strip().split(",")
for window in ranges:
    window = window.split("-")
    for i in range(int(window[0]), int(window[1]) + 1):
        id = str(i)
        if len(id) != length:
            length = len(id)
            factors = calculate(length)
 #           print(f"factors {factors}\nrange {window}, length {length}\n")
        for factor in factors:
            if (id[:factor[0]] * factor[1]) == id:
                total += int(id)
                break
print(total)