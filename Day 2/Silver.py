total = 0
count = 0
with open ("Text.txt", "r") as file:
    for line in file:
        count += 1
        safe = True
        assending = False


        row = line.replace("\n", "")
        row = row.split(" ")

       # print(f"{row} count of {count}")

        if int(row[0]) - int(row[1]) > 0:
            assending = False
        else:
            assending = True

        for i in range(len(row) - 1):
            difference = abs(int(row[i]) - int(row[i + 1]))
            if difference <= 3 and difference > 0:
                pass
            else:
                safe = False
       #         print(f"gap larger than 3, for values {row[i]} to {row[i + 1]}\n")
                break
            difference = (int(row[i]) - int(row[i + 1]))
            if difference > 0 and assending == True:
       #         print(f"should be decending caught assending for values {row[i]} to {row[i + 1]}\n")
                safe = False
                break
            elif difference < 0 and assending == False:
                safe = False
       #         print(f"should be decending caught assending for values {row[i]} to {row[i + 1]}\n")
                break
        if safe == True:
            total += 1
        
        

print(total)

