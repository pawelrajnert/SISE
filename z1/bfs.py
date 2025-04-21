import collections
import time

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
        visitedStateList = set()
        openStateList.append(startNode)
        visitedStateList.add(startNode)
        while time.time() - startTime < 60 and not foundGoal and len(openStateList) > 0:
            state = openStateList.popleft()
            nodesProcessed += 1
            state.createChildren(["L","R","U","D"])
            for child in state.children:
                if child not in visitedStateList:
                    maxDepth = max(maxDepth, child.nodeDepth)
                    if child.state == GOAL:
                        currentNode = child
                        foundGoal = True
                        break
                    openStateList.append(child)
                    visitedStateList.add(child)
        nodesVisited += len(visitedStateList)
    if currentNode.state == GOAL:
        return currentNode, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime
    else:
        return None, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime

