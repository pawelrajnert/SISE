import numpy as np

def prepareGoalBoard(startNode):
    rows = startNode.state.shape[0]
    cols = startNode.state.shape[1]
    numbers = list(range(1,rows*cols)) + [0]
    return np.array(numbers).reshape(rows,cols)

# w tej metryce sprawdzamy czy bloczek jest na swoim poprawnym miejscu, jeśli tak to nic nie robimy (odległość 0)
# ale jeśli bloczek jest na niepoprawnym miejscu to odległość będzie 1
def hamming(currentState):
    distance = 0
    goalBoard = prepareGoalBoard(currentState)

    for i in range(0, currentState.rowSize):
        for j in range(0, currentState.colSize):
            if currentState.state[i][j] == 0:  # zgodnie z informacją na zajęciach, ignorujemy bloczek 0 aby nie przeszacować wyniku
                continue

            if currentState.state[i][j] != goalBoard[i][j]:
                distance += 1

    return distance


# w tej metryce patrzymy jaka jest odległość bloczka od jego miejsca docelowego
def manhattan(currentState):
    distance = 0
    rowAmount = currentState.rowSize
    colAmount = currentState.colSize

    for i in range(0, rowAmount):
        for j in range(0, colAmount):
            if currentState.state[i][j] == 0:  # zgodnie z informacją na zajęciach, ignorujemy bloczek 0 aby nie przeszacować wyniku
                continue

            row = int((currentState.state[i][j] - 1) / colAmount)
            col = (currentState.state[i][j] - 1) % colAmount

            distance += abs(row - i) + abs(col - j)

    return distance