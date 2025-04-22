import time
from queue import PriorityQueue

from additionalMethods import *


def astar(startNode, strategy, heuristic):
    goalBoard = prepareGoalBoard(startNode)
    startTime = time.time()
    nodesVisited = 1
    nodesProcessed = 1
    maxDepth = 1
    foundGoal = False
    currentNode = startNode

    if not (startNode.state == goalBoard).all():
        closedStateList = set()
        openStateList = PriorityQueue()

        openStateList.put((0, startNode))  # wrzucamy początkowy element z priorytetem 0
        visitedStateList = set()

        while time.time() - startTime < 120 and not foundGoal and not openStateList.empty():
            visitedStateList = openStateList.get()
            nodesProcessed += 1

            if startNode.state == goalBoard:
                foundGoal = True
                return currentNode, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime

            currentNode.createChildren(strategy)

            if child not in visitedStateList:
                if child not in closedStateList:
                    openStateList.put(child)
                    # nodesProcessed += 1?

                for child in range(startNode.children):
                    if child not in closedStateList:
                        if heuristic == "hamming":
                            print("hamming")
                            functionF = 1  # testowo narazie

                    if heuristic == "manhattan":
                        print("manhattan")
                        functionF = 1  # tu tak samo

                openStateList.put((child, functionF))  # wedlug pseudokodu to tak (priorytet n i funkcja f)

    return False, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime
