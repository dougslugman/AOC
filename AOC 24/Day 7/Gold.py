import time
starttime = time.time()
total = 0
def tri(num, string=''):
    if num == 0:
        return string
    else:
        remainder = num % 3
        string = str(remainder) + string 
        return tri(num // 3, string)  
def generatetri(length):
    result = []
    for i in range(length, -1, -1):
        binary_length = len(tri(length))
        combination = (tri(i))
        result.append(combination.zfill(binary_length))
    return result
with open("Text.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line.split(':')
        line[1] = line[1].split(' ')
        line[1].pop(0)
        length = len(line[1]) - 1
        maximum = int((length * '2') , 3)
        results = generatetri(maximum)
        for i in range(len(results)):
            combo_sum = int(line[1][0])
            for j in range(len(results[i])):
                if results[i][j] == '0': 
                    combo_sum += int(line[1][j + 1])  
                elif results[i][j] == '1': 
                    combo_sum *= int(line[1][j + 1])
                elif results[i][j] == "2":
                    combo_sum = int(str(combo_sum) + line[1][j + 1])
            if combo_sum == int(line[0]):
                total += combo_sum
                break
endtime = time.time()
print(f"total was {total} with a time of {int(endtime) - int(starttime)} seconds")