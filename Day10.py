MAIN_CLOCK = 1
PIXEL_POS = 0
X_VALUE = 1
CurrentCommand = None
DELAYS = {}
MAX = 10
DELAYS["addx"] = 2
DELAYS["noop"] = 1
LAST_CHECK = 0

SIGNALS = [40,80,120, 160, 200, 240]
Values = []
#SIGNALS = [1,2,3,4,5,6]

def tickClock(num):
    global MAIN_CLOCK
    global  PIXEL_POS
    for x in range(0, num):
        if X_VALUE >= PIXEL_POS - 1 and X_VALUE <= PIXEL_POS + 1:
            print("#", end="")
        else:
            print(".", end="")
        if MAIN_CLOCK in SIGNALS:
            #end of Line
            print()
            PIXEL_POS = -1
            #Values.append(X_VALUE * MAIN_CLOCK)
            #print(str(MAIN_CLOCK) + "-" + str(X_VALUE) + ": " + str(X_VALUE * MAIN_CLOCK))
        PIXEL_POS += 1
        MAIN_CLOCK += 1


if __name__ == '__main__':
    with open("data/day10.txt") as inputFile:

        #READ EACH COMMAND
        for input in inputFile:
            #ADD INSTRUCTIONS
            if input.strip() == "noop":
                tickClock(DELAYS["noop"])
            else:
                cmd, value = input.strip().split(" ")
                tickClock(DELAYS["addx"])
                X_VALUE += int(value)
    #print("Finished at:" + str(MAIN_CLOCK))
    #print(sum(Values))



