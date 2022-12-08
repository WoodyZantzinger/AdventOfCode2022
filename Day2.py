
#A for Rock, B for Paper, and C for Scissors.
#X for Rock, Y for Paper, and Z for Scissors

Score = {}
Score["X"] = 1
Score["Y"] = 2
Score["Z"] = 3

RoundScore = {}
RoundScore["X"] = 0
RoundScore["Y"] = 3
RoundScore["Z"] = 6

Them = {}
Them["A"] = 1
Them["B"] = 2
Them["C"] = 3

# single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

if __name__ == '__main__':

    #Part 1
    totalScore = 0

    with open("data/day2.txt") as inputFile:
        for line in inputFile:
            outcomeScore = 0
            them, you = line.strip().split(" ")
            if you == "X": #we must lose
                if them == "A": outcomeScore = 3
                if them == "B": outcomeScore = 1
                if them == "C": outcomeScore = 2
            if you == "Y": #we must draw
                outcomeScore = Them[them]
            if you == "Z": #we must win
                if them == "A": outcomeScore = 2
                if them == "B": outcomeScore = 3
                if them == "C": outcomeScore = 1
            totalScore += (RoundScore[you] + outcomeScore)

    print(totalScore)
