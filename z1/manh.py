from additionalMethods import *

# w tej metryce patrzymy jaka jest odległość bloczka od jego miejsca docelowego
def manhattan(currentState):
    distance = 0
    goalBoard = prepareGoalBoard(currentState)

    for i in range(0, currentState.RowSize):
        for j in range(0, currentState.ColumnSize):
            if (currentState.state[i][j] == 0): # zgodnie z informacją na zajęciach, ignorujemy bloczek 0 aby nie przeszacować wyniku
                continue

            #xDistance = abs(goalBoard[i][j] - currentState.state[i][j])
            #yDistance = abs(goalBoard[j][i] - currentState.state[j][i])
            #distance += xDistance + yDistance

    return distance