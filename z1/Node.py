import numpy as np

class Node:
    def __init__(self, state, prevNode, moveToPrev, nodeDepth, zeroPos):
        self.state = state
        self.prevNode = prevNode
        self.moveToPrev = moveToPrev
        self.nodeDepth = nodeDepth
        self.zeroPos = zeroPos

        self.rowSize = self.state.shape[0]
        self.colSize = self.state.shape[1]

        self.children = []

    def createChildren(self, creationOrder):
        for element in creationOrder:
            x1, y1 = self.zeroPos
            x2, y2 = self.zeroPos
            if element == "L" and y1 > 0:
                y2 -= 1
            elif element == "R" and y1 < self.colSize - 1:
                y2 += 1
            elif element == "U" and x1 > 0:
                x2 -= 1
            elif element == "D" and x1 < self.rowSize - 1:
                x2 += 1
            else:
                continue
            stateCopy = self.state.copy()
            stateCopy[x1, y1], stateCopy[x2, y2] = self.state[x2, y2], self.state[x1, y1]
            newZeroPos = (x2, y2)
            childNode = Node(stateCopy, self, element, self.nodeDepth + 1, newZeroPos)
            self.children.append(childNode)


    def printState(self):
        print(str(self.state) + ", głębokość: " + str(self.nodeDepth) + ", pozycja zera: " + str(self.zeroPos) + ", ruch: " + str(self.moveToPrev))

    def __hash__(self):
        return hash(tuple(self.state.flatten()))

    def __eq__(self, other):
        return np.array_equal(self.state, other.state)
