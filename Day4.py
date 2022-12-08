


if __name__ == '__main__':

    with open("data/day4.txt") as inputFile:

        numOverlaps = 0
        for line in inputFile:
            #Sample line: "85-85,77-84"
            a1 = int(line.split(",")[0].split("-")[0])
            a2 = int(line.split(",")[0].split("-")[1])
            b1 = int(line.split(",")[1].split("-")[0])
            b2 = int(line.split(",")[1].split("-")[1])

            #is either A contained inbetween B1 and B2?
            if (a1 >= b1 and a1 <= b2) or (a2 >= b1 and a2 <= b2):
                numOverlaps += 1
                continue

            #is either B contained inbetween A1 and A2?
            if (b1 >= a1 and b1 <= a2) or (b2 >= a1 and b2 <= a2):
                numOverlaps += 1

        print(numOverlaps) #121 vs. 259 (too low). 459 was too high