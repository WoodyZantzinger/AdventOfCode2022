start_pos = [0,0]
end_pos = [0,0]
MainMap = None
Unexplored = []

class Map:
    def __init__(self, map, unexplored, start_pos):
        self.map = map
        self.unexplored = unexplored
        self.start_pos = start_pos

    def print(self):
        for row in self.map:
            for Node in row:
                print(str(Node.distance) + "\t", end = "")
            print()

    def getValidNeighbors(self, node):
        return_nodes = []
        values = [[-1,0], [1,0], [0,-1], [0,1]]
        for value in values:
            if node.x + value[0] < 0 or node.x + value[0] > len(self.map) - 1: continue
            if node.y + value[1] < 0 or node.y + value[1] > len(self.map[0]) - 1: continue
            test_node = self.map[node.x + value[0]][node.y + value[1]]
            if test_node not in self.unexplored: continue
            return_nodes.append(test_node)
        return return_nodes

    def getLowestUnexplored(self):
        lowest = 999999
        next_node = None
        #Did we explore everything?
        if len(self.unexplored) == 0: return None

        #else find the node with the current lowest pos
        for node in self.unexplored:
            if node.distance <= lowest:
                next_node = node
                lowest = node.distance

        #If we didn't find a starting node, start with the starting position Node
        if next_node == None: next_node = self.map[self.start_pos[0]][self.start_pos[1]]

        self.unexplored.remove(next_node)
        return next_node

    def get(self, x, y):
        return map[x][y]

class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.parent = None
        if value == "E": self.distance = 0
        else: self.distance = 999999
        self.x = x
        self.y = y

def tooLow(start, end):
    #For Part 2 this needs to be reversed
    if start == "S": start = "a"
    if start == "E": start = "z"
    if end == "E": end = "z"
    if ord(start) > ord(end) + 1: return True
    return False


if __name__ == '__main__':
    # Build Data Set
    temp_map = []
    with open("data/day12.txt") as inputFile:
        for x, line in enumerate(inputFile):
            row = []
            for y, height in enumerate(line.strip()):
                newNode = Node(height, x, y)
                if height == "E": start_pos = [x,y]
                elif height == "S": end_pos = [x, y]
                Unexplored.append(newNode)
                row.append(newNode)
            temp_map.append(row)
        MainMap = Map(temp_map, Unexplored, start_pos)

    nextNode = MainMap.getLowestUnexplored()
    while nextNode != None:

        #We done!
        #if nextNode.value == "E": break

        nodeNeighbors = MainMap.getValidNeighbors(nextNode)
        for neighbor in nodeNeighbors:
            #can we travel here?
            if not tooLow(nextNode.value, neighbor.value, ):
                newDist = nextNode.distance + 1
                if newDist < neighbor.distance:
                    neighbor.distance = newDist
                    neighbor.parent = nextNode

        #get new node
        nextNode = MainMap.getLowestUnexplored()

    #MainMap.print()
    Lowest = 999999
    for row in MainMap.map:
        for node in row:
            if node.value == "a":
                if node.distance < Lowest:
                    Lowest = node.distance
    print(Lowest)