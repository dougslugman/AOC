total = 0
windows = []
with open("Text2.txt", "r") as file:
    for line in file:
        line = list(map(int, line.strip().split("-")))
        windows.append(line)
overlap = 0
overlapped = [False for x in range(len(windows))]
for index, window in enumerate(windows):
    for check in windows:
        if window == check:
            continue
        if window[0] >= check[0] and check[1] >= window[1]:
            overlapped[index] = True
remove = []
for index, window in enumerate(windows):
    if overlapped[index]:
        overlap += window[1] - window[0] + 1
        remove.append(index)
remove.sort(reverse=True)
for r in remove:
    windows.pop(r)
def display(array):
    for item in array:
        print(item)
newranges = []
windows = sorted(windows, key=lambda x:x[0])
count = 0
length = len(windows)
while count < length:
    lowest = windows[count][0]
    highest = windows[count][1]
    if count+1 >= length:
        newranges.append([lowest, highest])
        break 
    while windows[count+1][0] <= highest:
        count+=1
        highest = windows[count][1]
    newranges.append([lowest, highest])
    count+=1
for window in newranges:
    total += window[1] - window[0] + 1
print(total)