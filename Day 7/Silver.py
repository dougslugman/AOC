total = 0
count = 0
def generate(length):
    result = []
    for i in range(length, -1, -1):
        binary_length = len(bin(length)[2:])
        combination = (bin(i)[2:])
        result.append(combination.zfill(binary_length))
    return result
with open("Text.txt", "r") as file:
    for line in file:
        count += 1
        line = line.strip()
        line = line.split(':')
        line[1] = line[1].split(' ')
        line[1].pop(0)
        length = len(line[1]) - 1
        maximum = int((length * '1') , 2)
        results = generate(maximum)
        for i in range(len(results)):
            combo_sum = int(line[1][0])
            for j in range(len(results[i])):
                if results[i][j] == '0': 
                    combo_sum += int(line[1][j + 1])  
                elif results[i][j] == '1': 
                    combo_sum *= int(line[1][j + 1])
            if combo_sum == int(line[0]):
                total += combo_sum
                break
print(total)

    





            
                

        
        


