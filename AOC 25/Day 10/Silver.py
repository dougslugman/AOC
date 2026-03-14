lights = []
correct = []
buttons = []
joltage = []
goal = ''
total = 0
with open("Text.txt", "r") as file:
    for line in file:
        line = line.strip().split(" ")
        lights.append(line[0].replace("[", "").replace("]", ""))
        joltage.append(line[-1].replace("{", "").replace("}", "").split(","))
        buttons.append([])
        for i, item in enumerate(line):
            if i == 0 or i == len(line)-1:
                continue
            buttons[-1].append(line[i].replace("(", "").replace(")", "").split(","))
def process(state, button):
    state = [x for x in state]
    for item in button:
        item = int(item)
        if state[item] == '#':
            state[item] = '.'
            continue
        state[item] = '#'
    state = ''.join(state)
    if state == goal:
        return True
    return state
for i in range(len(lights)):
    current = "."*len(lights[i])
    found = False
    queue = []
    count = 1
    goal = lights[i]
    for button in buttons[i]:
        queue.append([current, button])
    while not found:
        newqueue = []
        for item in queue:
            output = process(item[0], item[1])
            if output == True:
                found = True
                break
            newqueue.append(output)
        if found:
            continue
        queue = []
        for item in newqueue:
            for button in buttons[i]:
                queue.append([item, button])
        count+=1
    total += count
print(total)