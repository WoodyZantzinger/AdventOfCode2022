X_LENGTH = 100
Y_LENGTH = 100
HEAD_POS = (50,50)
TAIL_POS = (50,50)

moves = {}
moves["U"] = [-1, 0]
moves["D"] = [1, 0]
moves["L"] = [0, -1]
moves["R"] = [0, 1]

def pos_dif():
    return [HEAD_POS[0] - TAIL_POS[0],HEAD_POS[1]-TAIL_POS[1]]

spaces = {}

if __name__ == '__main__':

    #part 2
    with open("data/day9.txt") as inputFile:
        for line in inputFile:
            dir, amount = line.strip().split(" ")
            #print(line.strip())
            #For number of moves
            for itr in range(0, int(amount)):
                #Move head
                HEAD_POS = (HEAD_POS[0] + moves[dir][0], HEAD_POS[1] + moves[dir][1])
                #If the tail is too far away:
                diff = pos_dif()
                if abs(diff[0]) > 1 or abs(diff[1]) > 1:
                    #Do we need to go diag? 3 total spaces away means we're diagonal
                    if abs(diff[0]) + abs(diff[1]) > 2:
                        #find which direction (x or y) is only off by 1
                        if abs(diff[0]) == 1: TAIL_POS = (TAIL_POS[0] + diff[0], TAIL_POS[1])
                        else: TAIL_POS = (TAIL_POS[0], TAIL_POS[1] + diff[1] * 1)
                        diff = pos_dif()
                    #Now we need to Move tail LEFT, RIGHT, UP, DOWN
                    TAIL_POS = (int(TAIL_POS[0] + (diff[0]/2)), int(TAIL_POS[1] + (diff[1]/2)))

                    #Mark this space as seen
                    spaces[TAIL_POS] = True
                #print(str(HEAD_POS) + " -> " + str(TAIL_POS))
    #How many squares?
    print(len(spaces))