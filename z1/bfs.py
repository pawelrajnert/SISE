import collections
import time

from z1.Node import Node

GOAL = list(range(1,16)) + [0]
def bfs(startNode):
    startTime = time.time()
    nodesVisited = 1            # Uwzględniamy możliwość odwiedzenia i przetworzenia stanu początkowego
    nodesProcessed = 1          # W przypadku, gdy jest on stanem docelowym i nie wchodzimy w pętlę
    maxDepth = 1
    foundGoal = False
    currentNode = startNode
    if currentNode.state != GOAL:
        openStateList = collections.deque()
        closedStateList = set()
        openStateList.append(startNode)
        closedStateList.add(startNode)
        while time.time() - startTime < 60 and not foundGoal and len(openStateList) > 0:
            state = openStateList.popleft()
            nodesVisited += 1
            state.createChildren(["L","R","U","D"])
            for child in state.children:
                nodesProcessed += 1
                maxDepth = max(maxDepth, child.nodeDepth)
                if child not in closedStateList:
                    if child.state == GOAL:
                        currentNode = child
                        foundGoal = True
                        break
                    openStateList.append(child)
                    closedStateList.add(child)
    if currentNode.state == GOAL:
        return currentNode, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime
    else:
        return None, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime

