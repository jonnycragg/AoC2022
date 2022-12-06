def readData(file):
    player1Score = 0
    player2Score = 0
    playerScores = []  # Declare an empty list for player 1
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            # clean and read in turn data
            go = line.replace("\n", "").split(" ")
            print(go)
            # go through player turns and calculate score for each player and return player scores
            # A,X = Rock = 1 / B,Y = Paper = 2 / C,Y = Scissors = 3
            # 6 for a win and 0 for a loss
            # winner score = 6 + score of chosen rock 1, paper 2 or scissors 3
            # loser score = 0 + score of chosen rock 1, paper 2 or scissors 3
            # draw score = 3 + score of chosen rock 1, paper 2 or scissors 3
            go[0] = turn(go[0])
            go[1] = turn(go[1])
            if go[0] == go[1]:
                player1Score = player1Score + 3 + go[0]
                player2Score = player2Score + 3 + go[1]
            else:
                if beats(go[0],go[1]):
                    player1Score = player1Score + 6 + go[0]
                    player2Score = player2Score + 0 + go[1]
                else:
                    player1Score = player1Score + 0 + go[0]
                    player2Score = player2Score + 6 + go[1]
            print(player1Score, player2Score)
    return player1Score,player2Score

def readData_p2(file):
    player1Score = 0
    player2Score = 0
    playerScores = []  # Declare an empty list for player 1
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            # clean and read in turn data
            go = line.replace("\n", "").split(" ")
            print(go)
            # go through player turns and calculate score for each player and return player scores
            # A,X = Rock = 1 / B,Y = Paper = 2 / C,Y = Scissors = 3
            # 6 for a win and 0 for a loss
            # winner score = 6 + score of chosen rock 1, paper 2 or scissors 3
            # loser score = 0 + score of chosen rock 1, paper 2 or scissors 3
            # draw score = 3 + score of chosen rock 1, paper 2 or scissors 3
            go[0] = turn(go[0])
            go[1] = turn(go[1])
            # strategy!
            # X=1 means you need to lose
            # Y=2  means you need to end the round in a draw
            # and Z=3 means you need to win.
            if go[1] == 2:  #draw
                go[1] = go[0]
            else:
                if go[1] == 1:
                    if go[0] == 1: go[1] = 3
                    if go[0] == 2: go[1] = 1
                    if go[0] == 3: go[1] = 2
                else:
                    if go[0] == 1: go[1] = 2
                    if go[0] == 2: go[1] = 3
                    if go[0] == 3: go[1] = 1
            if go[0] == go[1]:
                player1Score = player1Score + 3 + go[0]
                player2Score = player2Score + 3 + go[1]
            else:
                if beats(go[0],go[1]):
                    player1Score = player1Score + 6 + go[0]
                    player2Score = player2Score + 0 + go[1]
                else:
                    player1Score = player1Score + 0 + go[0]
                    player2Score = player2Score + 6 + go[1]
            print(player1Score, player2Score)
    return player1Score,player2Score

def turn(go):
    if go == 'A': return 1
    if go == 'X': return 1
    if go == 'B': return 2
    if go == 'Y': return 2
    if go == 'C': return 3
    if go == 'Z': return 3

def beats(p1,p2):
    if p1 == 1 and p2 == 3: return True
    if p1 == 2 and p2 == 1: return True
    if p1 == 3 and p2 == 2: return True
    return False


if (__name__ == "__main__"):
    myInput = readData('../data/testinputDay2.txt')
    print(myInput)

    # X means you need to lose
    # Y means you need to end the round in a draw
    # and Z means you need to win.
    myInput = readData_p2('../data/inputDay2.txt')
    print(myInput)
