import time
from queue import PriorityQueue

from additionalMethods import *


def astar(startNode, strategy):
    goalBoard = prepareGoalBoard(startNode)
    startTime = time.time()
    nodesVisited = 1
    nodesProcessed = 1
    maxDepth = 1
    foundGoal = False
    currentNode = startNode

    closedStateList = set()
    openStateList = PriorityQueue()

    openStateList.put((0, startNode))  # wrzucamy początkowy element z priorytetem 0
    visitedStateList = set()

    while time.time() - startTime < 120 and not foundGoal and not openStateList.empty():
        visitedStateList = openStateList.get()
        nodesProcessed += 1

        if (currentNode.state == goalBoard).all():
            foundGoal = True
            return currentNode, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime

        currentNode.createChildren(strategy)

        for child in currentNode.children:
            if child not in visitedStateList:
                openStateList.put(child)
                # nodesVisited += 1?

                for child in range(currentNode.children):
                    if child not in closedStateList:
                        if strategy == "hamm":
                            functionF = currentNode.nodeDepth + hamming(currentNode)

                        if strategy == "manh":
                            functionF = currentNode.nodeDepth + manhattan(currentNode)

                openStateList.put((child, functionF))  # wedlug pseudokodu to tak (priorytet n i funkcja f)

    return None, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime
