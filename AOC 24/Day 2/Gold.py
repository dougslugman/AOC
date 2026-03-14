total = 0
count = 0


def issafe(row):
    safe = True
    assending = False

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
            return False
#         print(f"gap larger than 3, for values {row[i]} to {row[i + 1]}\n")
        difference = (int(row[i]) - int(row[i + 1]))
        if difference > 0 and assending == True:
#         print(f"should be decending caught assending for values {row[i]} to {row[i + 1]}\n")
            return False
        elif difference < 0 and assending == False:
            return False
#         print(f"should be decending caught assending for values {row[i]} to {row[i + 1]}\n")
    return True


with open ("Text.txt", "r") as file:
    for line in file:
        count += 1
        edit = line.replace("\n", "")
        edit = edit.split(" ")
        safe = issafe(edit)
        if safe == True:
            total+=1
            continue
        for i in range(len(edit)):
            temp = [edit[j] for j in range(len(edit)) if j != i]
            safe = issafe(temp)
            if safe == True:
                total+=1
                break

print(total)