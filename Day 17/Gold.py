import linecache
program = linecache.getline("Text.txt", 5).strip()
program = program.split(" ")[1].split(",")
program = [int(x) for x in program]

def getinp(program, answer, ind):
    if ind > len(program):
        return answer
    for b in range(8):
        a = (answer << 3) + b
        b = b ^ 2
        c = a >> b
        b = b ^ 3
        b = b ^ c
        if b % 8 == program[-(ind)]:
            some = getinp(program, a, ind+1)
            if some is not None:
                return some
    return None
            
print(getinp(program, program[-1], 1))