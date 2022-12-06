def readData(file):
    itemSum = 0
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            # clean and read in turn data
            line = [ch for ch in line.replace("\n", "")]
            comp1, comp2 = split_list(line)
            common = set(comp1) & set(comp2)
            lower = lowerAlphabet()
            upper = capitalAlphabet()
            item = list(common)[0]
            if item in upper: itemSum = itemSum + upper.index(item)+27
            if item in lower: itemSum = itemSum + lower.index(item)+1
            print(itemSum)
    print(lower)
    print(upper)
    return line

def readData_p2(file):
    print("Part 2")
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        # read 3 lines for the group and find what is in all 3 and accum index of that
        lower = lowerAlphabet()
        upper = capitalAlphabet()
        counter = 1
        itemSum = 0
        for line in myfile:  # For each line of text
            if counter == 1: mem1 = [ch for ch in line.replace("\n", "")]
            if counter == 2: mem2 = [ch for ch in line.replace("\n", "")]
            if counter == 3: mem3 = [ch for ch in line.replace("\n", "")]
            if counter == 3:
                counter = 0
                common = set(mem1) & set(mem2) & set(mem3)
                item = list(common)[0]
                if item in upper: itemSum = itemSum + upper.index(item)+27
                if item in lower: itemSum = itemSum + lower.index(item)+1
            counter = counter + 1
    return itemSum

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def lowerAlphabet():
    alphabets_in_lowercase = []
    for i in range(97, 123):
        alphabets_in_lowercase.append(chr(i))
    return alphabets_in_lowercase

def capitalAlphabet():
    alphabets_in_capital=[]
    for i in range(65,91):
        alphabets_in_capital.append(chr(i))
    return alphabets_in_capital


if (__name__ == "__main__"):
    myInput = readData('../data/testinputDay3.txt')
    #print(myInput)

    myInput = readData('../data/inputDay3.txt')
    #print(myInput)
    print(readData_p2('../data/inputDay3.txt'))
