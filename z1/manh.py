# w tej metryce patrzymy jaka jest odległość bloczka od jego miejsca docelowego
def manhattan(currentState):
    distance = 0
    rowAmount = currentState.rowSize
    colAmount = currentState.colSize

    for i in range(0, rowAmount):
        for j in range(0, colAmount):
            if currentState.state[i][j] == 0: # zgodnie z informacją na zajęciach, ignorujemy bloczek 0 aby nie przeszacować wyniku
                continue

            row = int((currentState.state[i][j] - 1) / colAmount)
            col = (currentState.state[i][j]-1) % colAmount

            distance += abs(row - i) + abs(col - j)

    return distance