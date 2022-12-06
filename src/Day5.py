def readData(file):
    itemSum = 0
    stacks = [['Z','N'],['M','C','D'],['P']]
    print(stacks)
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            # clean and read in turn data
            # move 1 from 2 to 1
            input = line.replace("\n", "").split(" ")
            print(input)
            move = int(input[1])
            fro = int(input[3])-1
            to = int(input[5])-1
            # rather than popping off end of stack just grab number on end of list and move then pop them off
            tempStack = stacks[fro]
            tempStack = tempStack[-move:]
            print(tempStack)
            for item in tempStack: stacks[to].append(item)
            for num in range(move): stacks[fro].pop()
            print(stacks)
    for stack in stacks: print(stack[-1])
    return line

def readData_p2(file):
    itemSum = 0
    stacks = [['Z','N'],['M','C','D'],['P']]
    stacks = [['W','M','L','F'],['B','Z','V','M','F'],['H','V','R','S','L','Q'],['F','S','V','Q','P','M','T','J'],['L','S','W'],['F','V','P','M','R','J','W'],['J','Q','C','P','N','R','F'],['V','H','P','S','Z','W','R','B'],['B','M','J','C','G','H','Z','W']]
    print(stacks)
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            # clean and read in turn data
            # move 1 from 2 to 1
            input = line.replace("\n", "").split(" ")
            move = int(input[1])
            fro = int(input[3])-1
            to = int(input[5])-1
            # rather than popping off end of stack just grab number on end of list and move then pop them off
            tempStack = stacks[fro]
            tempStack = tempStack[-move:]
            print(tempStack)
            for item in tempStack: stacks[to].append(item)
            for num in range(move): stacks[fro].pop()
            print(stacks)
    for stack in stacks: print(stack[-1])
    return line

if (__name__ == "__main__"):
    myInput = readData('../data/testinputDay5.txt')

    myInput = readData_p2('../data/inputDay5.txt')

RBTWJWMCF