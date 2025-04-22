import time
from queue import PriorityQueue
from additionalMethods import *

def astar(startNode, strategy):
    goalBoard = prepareGoalBoard(startNode)
    startTime = time.time()
    nodesVisited = 1
    nodesProcessed = 0
    currentDepth = 0

    openStateList = PriorityQueue()
    closedStateList = set()
    openStateList.put((0, nodesVisited, startNode))  # wrzucamy początkowy element z priorytetem 0

    while time.time() - startTime < 120 and not openStateList.empty():
        currentNode = openStateList.get()
        nodesProcessed += 1

        if (currentNode[2].state == goalBoard).all():
            return currentNode[2], nodesVisited, nodesProcessed, currentDepth, time.time() - startTime
        if currentNode[2] not in closedStateList:
            closedStateList.add(currentNode[2])
            currentNode[2].createChildren(["R", "L", "U", "D"])
            for child in currentNode[2].children:
                currentDepth = max(currentDepth, child.nodeDepth)
                if child not in closedStateList:
                    nodesVisited += 1
                    functionF = 0
                    if strategy == "hamm":
                        functionF = child.nodeDepth + hamming(child)

                    if strategy == "manh":
                        functionF = child.nodeDepth + manhattan(child)
                    openStateList.put(
                        (functionF, nodesVisited, child))  # wedlug pseudokodu to tak (priorytet n i funkcja f)

    return None, nodesVisited, nodesProcessed, currentDepth, time.time() - startTime