total = 0
with open("Text.txt", "r") as file:
    for _ in file:
        text = list(_)
        index = "".join(text).find("mul")
        while index != -1:
            cont = False
            if text[index + 3] != "(":
                index = "".join(text).find("mul", index + 1)
                continue
            start = index + 4  
            char = ''
            bracount = 0
            while char != ")" and start + bracount < len(text):
                char = text[start + bracount]
                bracount += 1
            end = start + bracount - 1  
            inbracket = text[start:end]  

            for i in range(len(inbracket)):
                if not inbracket[i].isdigit() and inbracket[i] != ',':
                    cont = True
                    break
            if cont:
                index = "".join(text).find("mul", index + 1)  
                continue
            sumstr = "".join(inbracket)  
            sumstr = sumstr.split(',')
            if len(sumstr) == 2 and sumstr[0].isdigit() and sumstr[1].isdigit():
                total += (int(sumstr[0]) * int(sumstr[1]))
            index = "".join(text).find("mul", index + 1)
print(total)