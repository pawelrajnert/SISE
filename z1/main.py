import random

import numpy as np

from Node import Node
from z1.bfs import bfs
from z1.dfs import dfs


def isMatrixGood(matrix):
    zeroPosition = ""
    uniqueElements = set()
    TAB_SIZE = len(matrix)
    if TAB_SIZE != 16:
        return False
    for i in range(TAB_SIZE):
        uniqueElements.add(matrix[i])
        if matrix[i] == 0:
            zeroPosition = i
    if len(uniqueElements) != TAB_SIZE or zeroPosition == "":
        return False
    return True, zeroPosition


def moveElement(move, matrix, zeroPos):
    if move == "L" and zeroPos % 4 != 0:
        matrix[zeroPos], matrix[zeroPos - 1] = matrix[zeroPos - 1], matrix[zeroPos]
        zeroPos -= 1
    elif move == "R" and zeroPos % 4 != 3:
        matrix[zeroPos], matrix[zeroPos + 1] = matrix[zeroPos + 1], matrix[zeroPos]
        zeroPos += 1
    elif move == "U" and zeroPos >= 4:
        matrix[zeroPos], matrix[zeroPos - 4] = matrix[zeroPos - 4], matrix[zeroPos]
        zeroPos -= 4
    elif move == "D" and zeroPos <= 11:
        matrix[zeroPos], matrix[zeroPos + 4] = matrix[zeroPos + 4], matrix[zeroPos]
        zeroPos += 4
    else:
        return False, zeroPos
    return True, zeroPos


def printMatrix(matrix):
    for i in range(0, len(matrix), 4):
        row = matrix[i:i + 4]
        print(" ".join(f"{num:4}" for num in row))


DIRECTIONS = ["L", "R", "U", "D"]


def bruteForceTest():  # zostawię ci, żebyś też przejrzał działanie - potem to wywalimy
    # TROCHĘ PRZEGLĄDAŁEM TYM SAM I WYDAJE MI SIĘ ŻE LOGIKA RUCHÓW DZIAŁA GIT, TYMCZASEM MY W CZWARTEK O 21:00 - (:
    testMatrix = list(range(16))
    random.shuffle(testMatrix)
    _, zeroPos = isMatrixGood(testMatrix)
    print("Pozycja zera: " + str(zeroPos) + ", stan początkowy: ")
    printMatrix(testMatrix)
    movesMade = list()
    for _ in range(100000):       # zmień sobie na ludzką liczbę typu 5-10, bruteForce bo patrzę czy nie wywala programu XDDDDD
        random.shuffle(testMatrix)      # zakomentuj/wywal by patrzeć na pojedynczy ruch na jednej planszy - to jest dla tzw bruteForce
        move = random.choice(DIRECTIONS)
        # print("Próbuję wykonać ruch: " + move + ", pozycja zera: " + str(zeroPos))        odkomentuj jak chcesz każdy ruch z osobna analizować
        result, zeroPos = moveElement(move, testMatrix, zeroPos)
        # do końca sobie odkomentuj - by analizować ruchy z osobna
        # if result:
            # printMatrix(testMatrix)
            # movesMade.append(move)
        #else: print("nope")
    print("Wynik testu: ")
    printMatrix(testMatrix)
    # print("Wynikowa pozycja zera: " + str(zeroPos) + ", wykonane ruchy: ", end="")
    # for move in movesMade:
    #    print(move, end="")

#bruteForceTest()

def findZeroAndVerify(array):
    rows = array.shape[0]
    cols = array.shape[1]
    if set(array.flatten()) != set(range(rows * cols)):
        raise ValueError("Wprowadzony układ jest nieprawidłowy!")
    for row in range(array.shape[0]):
        for col in range(array.shape[1]):
            if array[row, col] == 0:
                return row, col
    return None, None

state = np.array([[5, 1, 7, 3],
                  [9, 2, 6, 4],
                  [13, 10, 11, 8],
                  [0, 14, 15, 12]])

startState = Node(state, None, None, 0, findZeroAndVerify(state))
result = dfs(startState)
if result[0] is None:
    print(-1)
else:
    results = []
    resultNode = result[0]
    while resultNode is not startState:
        results.append(resultNode.moveToPrev)
        resultNode = resultNode.prevNode
    print(len(results))
    for r in reversed(results):
        print(r, end="")
    print()
    print("Liczba węzłów odwiedzonych: " + str(result[1]))
    print("Liczba węzłów przetworzonych " + str(result[2]))
    print("Maksymalna głębokość rekursji: " + str(result[3]))
    print("Czas: " + str(result[4]))