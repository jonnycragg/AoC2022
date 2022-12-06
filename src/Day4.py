def readData(file):
    itemSum = 0
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            # clean and read in turn data
            sections = split_list(line.replace("\n", "").split(","))
            set1 = set(sections[0])
            set2 = set(sections[1])
            if (set1.issubset(set2)) | (set2.issubset(set1)):
                print(set1, set2)
                print("fully in the other")
                itemSum = itemSum + 1
    print(itemSum)
    return line

def readData_p2(file):
    itemSum = 0
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            # clean and read in turn data
            sections = split_list(line.replace("\n", "").split(","))
            set1 = set(sections[0])
            set2 = set(sections[1])
            if set1.intersection(set2): itemSum = itemSum + 1
    print(itemSum)
    return line

def split_list(list):  #e.g. 1-2,4-5
    ranges = []
    for a_list in list:
        st, end = a_list.split("-")
        ranges.append([*range(int(st), int(end)+1)])
    return ranges


if (__name__ == "__main__"):
    myInput = readData('../data/testinputDay4.txt')
    myInput = readData('../data/inputDay4.txt')

    myInput = readData_p2('../data/testinputDay4.txt')
    myInput = readData_p2('../data/inputDay4.txt')
