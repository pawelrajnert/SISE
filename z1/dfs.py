import time

GOAL = list(range(1,16)) + [0]

def dfs(startNode):
    startTime = time.time()
    nodesVisited = 1            # Uwzględniamy możliwość odwiedzenia i przetworzenia stanu początkowego
    nodesProcessed = 1          # W przypadku, gdy jest on stanem docelowym i nie wchodzimy w pętlę
    maxDepth = 1
    currentNode = startNode
    foundGoal = False
    if startNode.state != GOAL:
        openStateList = list()
        closedStateList = set()
        openStateList.append(startNode)
        while time.time() - startTime < 60 and len(openStateList) > 0 and not foundGoal:
            currentNode = openStateList.pop()
            nodesProcessed += 1
            if currentNode.nodeDepth < 15 and currentNode not in closedStateList:
                closedStateList.add(currentNode)
                currentNode.createChildren(["R","D","L","U"])
                for child in reversed(currentNode.children):
                    maxDepth = max(maxDepth, child.nodeDepth)
                    if child.state == GOAL:
                        currentNode = child
                        foundGoal = True
                        break
                    if child not in closedStateList:
                        nodesVisited += 1
                        openStateList.append(child)
    if currentNode.state == GOAL:
        return currentNode, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime
    else:
        return None, nodesVisited, nodesProcessed, maxDepth, time.time() - startTime