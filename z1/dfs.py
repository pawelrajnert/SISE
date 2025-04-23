import time
from additionalMethods import prepareGoalBoard


def dfs(startNode, strategy):
    goalBoard = prepareGoalBoard(startNode)
    startTime = time.time()
    nodesVisited = 1  # Uwzględniamy możliwość odwiedzenia i przetworzenia stanu początkowego
    nodesProcessed = 1  # W przypadku, gdy jest on stanem docelowym i nie wchodzimy w pętlę
    currentDepth = 0
    currentNode = startNode
    foundGoal = False

    if not (startNode.state == goalBoard).all():
        openStateList = list()
        closedStateList = set()
        openStateList.append(startNode)

        while time.time() - startTime < 120 and len(openStateList) > 0 and not foundGoal:
            currentNode = openStateList.pop()
            nodesProcessed += 1

            if currentNode.nodeDepth < 21 and currentNode not in closedStateList:
                closedStateList.add(currentNode)
                currentNode.createChildren(strategy)

                for child in reversed(currentNode.children):
                    currentDepth = max(currentDepth, child.nodeDepth)

                    if (child.state == goalBoard).all():
                        currentNode = child
                        foundGoal = True

                    if child not in closedStateList:
                        nodesVisited += 1
                        openStateList.append(child)

    if (currentNode.state == goalBoard).all():
        return currentNode, nodesVisited, nodesProcessed, currentDepth, time.time() - startTime

    else:
        return None, nodesVisited, nodesProcessed, currentDepth, time.time() - startTime
