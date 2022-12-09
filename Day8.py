import numpy as np
Trees = []

if __name__ == '__main__':

    #Build Data Set
    with open("data/day8.txt") as inputFile:
        for line in inputFile:
            row = []
            for tree in line.strip():
                row.append([int(tree), False])
            Trees.append(row)

    maxX = range(len(Trees))
    maxY = range(len(Trees[0]))

    angles = [[maxX, maxY, True], [list(reversed(maxX)), maxY, False], [maxX, list(reversed(maxY)), True], [maxX, list(reversed(maxY)), False]]
    total = 0

    for angle in angles:
        for x in angle[0]:
            tallestTree = -1
            for y in angle[1]:
                if(angle[2]): tree = Trees[x][y]
                else:  tree = Trees[y][x]
                if tree[0] > tallestTree:
                    if not tree[1]: total += 1
                    tree[1] = True
                    tallestTree = tree[0]
        #print(total)
    print(total) #question 1 Total

    #for every square

    best_view = 0
    for start_x in maxX:
        for start_y in maxY:
#            start_x = 3
#            start_y = 2
            starting_height = Trees[start_x][start_y][0]
            sums = [0,0,0,0]
            #calculate in every direction
            for x in list(reversed(range(0, start_x))):
                sums[0] += 1
                if Trees[x][start_y][0] >= starting_height: break

            for x in range(start_x+1, len(maxX)):
                sums[1] += 1
                if Trees[x][start_y][0] >= starting_height: break

            for y in list(reversed(range(0, start_y))):
                sums[2] += 1
                if Trees[start_x][y][0] >= starting_height: break

            for y in range(start_y+1, len(maxY)):
                sums[3] += 1
                if Trees[start_x][y][0] >= starting_height: break

            view = sums[0] * sums[1] * sums[2] * sums[3]
            if view > best_view:
                best_view = view

    print(best_view)

    for row in Trees:
        for tree in row:
            if tree[1]:
                print(tree[0], end=" ")
            else: print("x", end=" ")
        print("")
