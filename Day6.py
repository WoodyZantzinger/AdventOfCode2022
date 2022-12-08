
def numOccurances(letter, string):
    index = 0
    instances = 0
    while string.find(letter, index) >= 0:
        instances += 1
        index = string.find(letter, index) + 1
    return instances

def allUnique(string):
    for letter in string:
        if numOccurances(letter, string) > 1: return False
    return True


if __name__ == '__main__':
    with open("data/day6.txt") as inputFile:
        dataBuffer = inputFile.readline()
        trailing4 = ""
        index = 0
        for character in dataBuffer:
            index += 1
            trailing4 += character
            if len(trailing4) < 14: continue
            if len(trailing4) > 14: trailing4 = trailing4[1:]
            if allUnique(trailing4):
                print(index)
                break

