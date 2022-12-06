def readData(file):
    itemSum = 0
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            input = line.replace("\n", "")
            # read in first 4 and check if unique, if not then read fron 2nd char then ext 4 and check
            index = 0
            found = False
            while not found:
                check = input[index:index+14]
                print(check)
                if len(set(check)) == len(check): found = True
                index = index +1
            print("Found these 4 chars:" + str(check))
            print("Index =" + str(index+13))
    return line

if (__name__ == "__main__"):
    myInput = readData('../data/testinputDay6.txt')
    myInput = readData('../data/inputDay6.txt')
