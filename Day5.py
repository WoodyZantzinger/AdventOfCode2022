#day5

END_OF_INIT = 8
NUMBER_OF_STACKS = 9

ArrayofStack = []
for x in range(NUMBER_OF_STACKS):
    ArrayofStack.append([])

def ParseStacks():
    with open("data/day5.txt") as inputFile:
        head = [next(inputFile) for x in range(END_OF_INIT)]
    list.reverse(head)
    #Go through each row of the file, move through the offsets (1,5,9,13 etc.) and create lists
    for row in head:
        for x in range(NUMBER_OF_STACKS):
            try:
                offset = 1 + (4*x)
                if(row[offset]) != " ":
                    ArrayofStack[x].append(row[offset])
            except IndexError:
                continue #Further stacks in this row don't have boxes

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ParseStacks()
    #print(ArrayofStack)
    with open("data/day5.txt") as inputFile:
        for i in range(END_OF_INIT + 2): #Skip the intro area
            next(inputFile)
        for line in inputFile:
            #N times, pop from A and append to B
            source = int(line.split(" ")[3]) - 1
            dest = int(line.split(" ")[5]) - 1
            N = int(line.split(" ")[1])
            tempArray = []
            for x in range(N):
                tempArray.append(ArrayofStack[source].pop())
            list.reverse(tempArray)
            for x in tempArray:
                ArrayofStack[dest].append(x)
    print(ArrayofStack)
    for stack in ArrayofStack:
        print(stack.pop())


