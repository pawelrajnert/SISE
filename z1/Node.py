DIRECTIONS = ["L", "R", "U", "D"]
import random

class Node:
    def __init__(self, state, prevNode, moveToPrev, nodeDepth):
        self.state = state
        self.prevNode = prevNode
        self.moveToPrev = moveToPrev
        self.nodeDepth = nodeDepth
        self.zeroPos = None
        self.children = []
        self.findZero()

    def findZero(self):
        if len(self.state) != 16:
            raise ValueError("Stan musi mieć 16 elementów!")
        if set(self.state) != set(range(16)):
            raise ValueError("Stan nie jest permutacją liczb od 0 do 15!")
        for i in range(16):
            if self.state[i] == 0:
                self.zeroPos = i
                break

    def createChildren(self, creationOrder):
        for element in creationOrder:
            stateCopy = self.state.copy()
            if element == "L" and self.zeroPos % 4 != 0:
                stateCopy[self.zeroPos], stateCopy[self.zeroPos - 1] = stateCopy[self.zeroPos - 1], stateCopy[self.zeroPos]
            elif element == "R" and self.zeroPos % 4 != 3:
                stateCopy[self.zeroPos], stateCopy[self.zeroPos + 1] = stateCopy[self.zeroPos + 1], stateCopy[self.zeroPos]
            elif element == "U" and self.zeroPos >= 4:
                stateCopy[self.zeroPos], stateCopy[self.zeroPos - 4] = stateCopy[self.zeroPos - 4], stateCopy[self.zeroPos]
            elif element == "D" and self.zeroPos <= 11:
                stateCopy[self.zeroPos], stateCopy[self.zeroPos + 4] = stateCopy[self.zeroPos + 4], stateCopy[self.zeroPos]
            if stateCopy != self.state:
                childNode = Node(stateCopy, self, element, self.nodeDepth + 1)
                self.children.append(childNode)


    def printState(self):
        for i in range(0, len(self.state), 4):
            row = self.state[i:i + 4]
            print(" ".join(f"{num:4}" for num in row))
        print(self.zeroPos)

    def __hash__(self):
        return hash(tuple(self.state))

    def __eq__(self, other):
        return self.state == other.state
