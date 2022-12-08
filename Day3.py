
def fetchScore(letter):
    if letter.isupper(): return ord(letter) - 38
    if letter.islower(): return ord(letter) - 96

if __name__ == '__main__':

    #Part 1
    with open("data/day3.txt") as inputFile:
        total = 0
        for line in inputFile:
            line = line.strip()
            middle = int(len(line) / 2)
            part1, part2 = line[:middle], line[middle:]

            for item in part1:
                if part2.find(item) < 0: continue #This item wasn't in both sack, skip
                #found overlap item
                total += fetchScore(item)
                break
        print(total)
        # 10546 was too high, 7618 too low

    #Part 2
    with open("data/day3.txt") as inputFile:

        stringGroup = []
        total = 0
        while True:
            line = inputFile.readline()
            if not line: break
            stringGroup.append(line.strip())
            if len(stringGroup) == 3:
                for item in stringGroup[0]:
                    in1 = stringGroup[1].find(item) > -1
                    in2 = stringGroup[2].find(item) > -1
                    if in1 and in2:
                        total += fetchScore(item)
                        break
                stringGroup = []

        print(total)
        # too high 3904
