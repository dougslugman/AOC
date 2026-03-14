import math
total = 0
with open("Test.txt", "r") as file:
    rega = (file.readline()).strip().split(" ")
    rega.pop(0)
    rega.pop(0)
    rega = int(rega[0])
    regb = (file.readline()).strip().split(" ")
    regb.pop(0)
    regb.pop(0)
    regb = int(regb[0])
    regc = (file.readline()).strip().split(" ")
    regc.pop(0)
    regc.pop(0)
    regc = int(regc[0])
    file.readline()
    program = file.readline().split(" ")
    program = program[1].split(",")
    program = [int(x) for x in program]
pointer = 0
output = []
while pointer < len(program):
    #get opcode
    opcode = program[pointer]
    #get literal operand
    litrand = program[pointer + 1]
    #get combo operand
    if litrand >= 0 and litrand < 4:
        comrand = litrand
    elif litrand == 4:
        comrand = rega
    elif litrand == 5:
        comrand = regb
    elif litrand == 6:
        comrand = regc
    else:
        print("invalid program")
        exit()
    if opcode == 0:
        neum = rega
        deno = (2**comrand)
        rega = neum//deno
    elif opcode == 1:
        regb = (regb ^ litrand)
    elif opcode == 2:
        regb = (comrand % 8)
    elif opcode == 3:
        if rega != 0:
            pointer = litrand
            continue
    elif opcode == 4:
        regb = regb ^ regc
    elif opcode == 5:
        output.append(comrand % 8)
    elif opcode == 6:
        neum = rega
        deno = (2**comrand)
        regb = neum//deno
    elif opcode == 7:
        neum = rega
        deno = (2**comrand)
        regc = neum//deno
    else:
        print("opcode was above 7")
        exit()
    pointer += 2
output = [str(x) + "," for x in output]
total = ''.join(output).rstrip(',')
print(total)
