from additionalMethods import *

# w tej metryce sprawdzamy czy bloczek jest na swoim poprawnym miejscu, jeśli tak to nic nie robimy (odległość 0)
# ale jeśli bloczek jest na niepoprawnym miejscu to odległość będzie 1
def hamming(currentState):
    distance = 0
    goalBoard = prepareGoalBoard(currentState)

    for i in range(0, currentState.rowSize):
        for j in range(0, currentState.colSize):
            if currentState.state[i][j] == 0: # zgodnie z informacją na zajęciach, ignorujemy bloczek 0 aby nie przeszacować wyniku
                continue

            if currentState.state[i][j] != goalBoard[i][j]:
                distance += 1

    return distance
