class Directory:
    def __init__(self, name):
        self.files = []
        self.name = name
        self.parent_directory = None
        self.child_directory = []

    def returnChild(self, name):
        for child in self.child_directory:
            if child.name == name: return child
        return None

    def addChild(self, dir):
        dir.parent_directory = self
        self.child_directory.append(dir)

    def getSize(self):
        final_size = 0
        for dir in self.child_directory:
            final_size += dir.getSize()
        for file in self.files:
            final_size += file.size
        return final_size

class File:
    def __init__(self, size, name):
        self.name = name
        self.size = int(size)

def findSmall(listOfDirectories):
    sub10 = []
    for d in listOfDirectories:
        if d.getSize() <= 100000:
            sub10.append(d)
        sub10.extend(findSmall(d.child_directory))
    return sub10

def findOverSize(listOfDirectories, size):
    sub10 = []
    for d in listOfDirectories:
        if d.getSize() >= size:
            sub10.append(d)
        sub10.extend(findOverSize(d.child_directory, size))
    return sub10

if __name__ == '__main__':
    Root = Directory("/")
    CurrentDir = Root
    #create a tree of directories and files
    with open("data/day7.txt") as inputFile:
        next(inputFile) #Skip line 1
        for line in inputFile:
            line = line.strip()
            if line.startswith("$ ls"): #Do nothing on LS lines, we should already be in the direct directory
                continue

            elif line.startswith("dir"): #This is a new directory, add to tree
                CurrentDir.addChild(Directory(line.split(" ")[1]))

            elif line.startswith("$ cd"): #we're changing directory, up or down
                dest = line.split(" ")[2]
                if dest == "..":
                    CurrentDir = CurrentDir.parent_directory
                else: CurrentDir = CurrentDir.returnChild(dest)

            else: #this line must be a file
                CurrentDir.files.append(File(line.split(" ")[0], line.split(" ")[1]))
    finals = findSmall([Root])
    totalSize = 0
    for f in finals: totalSize += f.getSize()
    print(totalSize) #Answer to Q 1
    FreeSpace = (70000000 - Root.getSize())
    RequiredSpace = 30000000 - FreeSpace

    #get every directory over required size
    finals = findOverSize([Root], RequiredSpace)
    BestFit = None
    for f in finals:
        if BestFit == None: BestFit = f
        if f.getSize() < BestFit.getSize(): BestFit = f #Find the smallest directory in the set

    #Print size of smallest directory
    print(str(RequiredSpace) + " space needed. Delete: " + str(BestFit.getSize()))

