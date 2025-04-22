import collections
import time

from additionalMethods import prepareGoalBoard

def bfs(startNode, strategy):
    goalBoard = prepareGoalBoard(startNode)
    startTime = time.time()
    nodesVisited = 1            # Uwzględniamy możliwość odwiedzenia i przetworzenia stanu początkowego
    nodesProcessed = 1          # W przypadku, gdy jest on stanem docelowym i nie wchodzimy w pętlę
    currentDepth = 0
    foundGoal = False
    currentNode = startNode
    if not (currentNode.state == goalBoard).all():
        openStateList = collections.deque()
        visitedStateList = set()
        openStateList.append(startNode)
        visitedStateList.add(startNode)
        while time.time() - startTime < 120 and not foundGoal and len(openStateList) > 0:
            state = openStateList.popleft()
            nodesProcessed += 1
            state.createChildren(strategy)
            for child in state.children:
                if child not in visitedStateList:
                    currentDepth = max(currentDepth, child.nodeDepth)
                    if (child.state == goalBoard).all():
                        currentNode = child
                        foundGoal = True
                    openStateList.append(child)
                    visitedStateList.add(child)
        nodesVisited = len(visitedStateList)
    if (currentNode.state == goalBoard).all():
        return currentNode, nodesVisited, nodesProcessed, currentDepth, time.time() - startTime
    else:
        return None, nodesVisited, nodesProcessed, currentDepth, time.time() - startTime

