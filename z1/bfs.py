import collections
import time

import numpy as np

GOAL = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,0]])
def bfs(startNode):
    startTime = time.time()
    nodesVisited = 1            # Uwzględniamy możliwość odwiedzenia i przetworzenia stanu początkowego
    nodesProcessed = 1          # W przypadku, gdy jest on stanem docelowym i nie wchodzimy w pętlę
    maxDepth = 1
    foundGoal = False
    currentNode = startNode
    if not (currentNode.state == GOAL).all():
        openStateList = collections.deque()
        visitedStateList = set()
        openStateList.append(startNode)
        visitedStateList.add(startNode)
        while time.time() - startTime < 60 and not foundGoal and len(openStateList) > 0:
            state = openStateList.popleft()
            nodesProcessed += 1
            state.createChildren(["R", "D", "L", "U"])
            for child in state.children:
                if child not in visitedStateList:
                    maxDepth = max(maxDepth, child.nodeDepth)
                    if (child.state == GOAL).all():
                        currentNode = child
                        foundGoal = True
                        break
                    openStateList.append(child)
                    visitedStateList.add(child)
        nodesVisited += len(visitedStateList)
    if (currentNode.state == GOAL).all():
        return currentNode, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime
    else:
        return None, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime

