import collections

GOAL = list(range(1,16)) + [0]
print(GOAL)

def bfs(startState):
    openStateList = collections.deque()
    closedStateList = set()
    if startState.state == GOAL:
        return startState
    openStateList.append(startState)
    closedStateList.add(startState)
    while len(openStateList) > 0:
        state = openStateList.popleft()
        state.createChildren(["L","R","U","D"])
        for child in state.children:
            if child not in closedStateList:
                if child.state == GOAL:
                    return child
                openStateList.append(child)
                closedStateList.add(child)
    return False

