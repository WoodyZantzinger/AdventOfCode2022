X_LENGTH = 100
Y_LENGTH = 100
HEAD_POS = (50,50)
TAIL_POS = []
for x in range(0,9):
    TAIL_POS.append( (50,50) )

moves = {}
moves["U"] = [-1, 0]
moves["D"] = [1, 0]
moves["L"] = [0, -1]
moves["R"] = [0, 1]

def pretty_print():
    for x in range(HEAD_POS[0] - 10, HEAD_POS[0] + 10):
        for y in range(HEAD_POS[1] - 10, HEAD_POS[1] + 10):
            pos = (x, y)
            Empty = True
            if HEAD_POS == pos:
                print("H", end="")
                continue
            for tail_num, tail in enumerate(TAIL_POS):
                if tail == pos:
                    print(str(tail_num+1).capitalize(), end="")
                    Empty = False
                    break
            if Empty: print(". ", end="")
            else: print(" ", end="")
        print(" ")


def pos_dif(x, y):
    return [x[0] - y[0],x[1]-y[1]]

spaces = {}

if __name__ == '__main__':

    #part 2
    with open("data/day9.txt") as inputFile:
        for line in inputFile:
            dir, amount = line.strip().split(" ")
            print(line.strip())

            #For number of moves
            for itr in range(0, int(amount)):
                #Move head
                HEAD_POS = (HEAD_POS[0] + moves[dir][0], HEAD_POS[1] + moves[dir][1])

                # move EACH tail
                for x in range(0, len(TAIL_POS)):
                    #If the tail is too far away:
                    if x == 0: diff = pos_dif(HEAD_POS, TAIL_POS[x])
                    else: diff = pos_dif(TAIL_POS[x-1], TAIL_POS[x])

                    if abs(diff[0]) + abs(diff[1]) == 4:
                        TAIL_POS[x] = (TAIL_POS[x][0] + diff[0] / 2, TAIL_POS[x][1] + diff[1] / 2)
                        continue
                    if abs(diff[0]) > 1 or abs(diff[1]) > 1:
                        #Do we need to go diag? 3 total spaces away means we're diagonal
                        if abs(diff[0]) + abs(diff[1]) == 3:
                            #find which direction (x or y) is only off by 1
                            if abs(diff[0]) == 1: TAIL_POS[x] = (TAIL_POS[x][0] + diff[0], TAIL_POS[x][1])
                            else: TAIL_POS[x] = (TAIL_POS[x][0], TAIL_POS[x][1] + diff[1])

                        if x == 0:
                            diff = pos_dif(HEAD_POS, TAIL_POS[x])
                        else:
                            diff = pos_dif(TAIL_POS[x - 1], TAIL_POS[x])
                        #Now we need to Move tail LEFT, RIGHT, UP, DOWN
                        TAIL_POS[x] = (int(TAIL_POS[x][0] + (diff[0]/2)), int(TAIL_POS[x][1] + (diff[1]/2)))

                #Mark this space as seen
                spaces[TAIL_POS[8]] = True
                #pretty_print()
                #print("-----")
    #How many squares?
    print(len(spaces))