def readData(file):
    myElfs = []  # Declare an empty list
    elfcounter = 0
    elfCalories = 0
    biggest = 0
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            # clean line
            cleanline = line.replace(" ", "").replace("\n", "")
            # if number then accumulate it until blank line
            print("Ellie, this line =" + cleanline)
            if (cleanline == ""):
                myElfs.append(elfCalories)
                elfcounter = elfcounter + 1
                if elfCalories > biggest:
                    biggest = elfCalories
                    biggestElf = elfcounter
                elfCalories = 0
            else:
                elfCalories = elfCalories + int(cleanline)
            # print(cleanline)
        # when end of line catch the last elf
        myElfs.append(elfCalories)
        print("Ellie elf list=" + str(myElfs))
        print(biggestElf, " ", biggest)
    return myElfs


if (__name__ == "__main__"):
    myInput = readData('../data/testinputDay1.txt')
    myInput.sort(reverse=True)
    print("Ellie biggest 3 = " + str(myInput))
    print(myInput[0]+myInput[1]+myInput[2])

    myInput = readData('../data/inputDay1.txt')
    myInput.sort(reverse=True)
    print(myInput)
    print(myInput[0]+myInput[1]+myInput[2])
