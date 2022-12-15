import math

MONKEYS = []
MAX_ROUNDS = 20

class monkey():
    def __init__(self, num, items, operation, divisible, ifTrue, ifFalse):
        self.num = num
        self.items = items
        self.operation = operation
        self. divisible = divisible
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse
        self.num_inspects = 0

    def addItem(self, item):
        self.items.append(item)

    def holding(self):
        print("Monkey " + str(self.num) + ": " + str(self.items))

    def inspectItems(self):
        global MONKEYS
        to_remove = []
        for item in self.items:
            self.num_inspects += 1
            #print("\tMonkey inspects item with worry level " + str(item))
            old = int(item)
            new = eval(self.operation.split(" = ")[1])
            #print("\t\tNew worry level is " + str(new))
            #new = math.floor(new / 3)
            #print("\t\tBored down to " + str(new))
            if (new % self.divisible) == 0:
                #print("\t\tWas divisible by " + str(self.divisible))
                MONKEYS[self.ifTrue].addItem(new)
                #print("\t\tThrown to " + str(self.ifTrue))
            else:
                #print("\t\tWas NOT divisible by " + str(self.divisible))
                MONKEYS[self.ifFalse].addItem(new)
                #print("\t\tThrown to " + str(self.ifFalse))
            to_remove.append(item)
        for item in to_remove:
            self.items.remove(item)


if __name__ == '__main__':
    with open("data/day11.txt") as inputFile:

        #Parse the Monkeys
        while True:
            if inputFile.readline().strip().startswith("Monkey"):
                num = len(MONKEYS)
                input = inputFile.readline().strip()
                items = input.strip()[16:].split(", ")

                input = inputFile.readline().strip()
                operation = input.strip()[11:]

                input = inputFile.readline().strip()
                divisible = int(input.strip()[19:])

                input = inputFile.readline().strip()
                ifTrue = int(input.strip()[25:])

                input = inputFile.readline().strip()
                ifFalse = int(input.strip()[26:])
                MONKEYS.append(monkey(num, items, operation, divisible, ifTrue, ifFalse))
            if not inputFile.readline(): break

    for rounds in range(0, MAX_ROUNDS):
        if rounds % 10 == 0:
            print(rounds)
            print(MONKEYS[0].items)
        for monkey in iter(MONKEYS):
            #print("Monkey " + str(monkey.num))
            monkey.inspectItems()

    insp = []
    for monkey in MONKEYS:
        #monkey.holding()
        insp.append(monkey.num_inspects)
    insp.sort()
    insp.reverse()
    print(insp[0] * insp[1])