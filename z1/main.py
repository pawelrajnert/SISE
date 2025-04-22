import random

import numpy as np
import sys

from Node import Node
from bfs import bfs
from dfs import dfs
from hamm import *
from manh import *
from astr import *


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
    for _ in range(
            100000):  # zmień sobie na ludzką liczbę typu 5-10, bruteForce bo patrzę czy nie wywala programu XDDDDD
        random.shuffle(
            testMatrix)  # zakomentuj/wywal by patrzeć na pojedynczy ruch na jednej planszy - to jest dla tzw bruteForce
        move = random.choice(DIRECTIONS)
        # print("Próbuję wykonać ruch: " + move + ", pozycja zera: " + str(zeroPos))        odkomentuj jak chcesz każdy ruch z osobna analizować
        result, zeroPos = moveElement(move, testMatrix, zeroPos)
        # do końca sobie odkomentuj - by analizować ruchy z osobna
        # if result:
        # printMatrix(testMatrix)
        # movesMade.append(move)
        # else: print("nope")
    print("Wynik testu: ")
    printMatrix(testMatrix)
    # print("Wynikowa pozycja zera: " + str(zeroPos) + ", wykonane ruchy: ", end="")
    # for move in movesMade:
    #    print(move, end="")


# bruteForceTest()

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


def readBoardFromFile():
    sourceFile = sys.argv[3]
    openSourceFile = open(sourceFile, "r")
    readText = openSourceFile.read()
    readText = readText.split()
    rows = int(readText[0])
    cols = int(readText[1])
    values = list(map(int, readText[2:]))
    array = np.array(values).reshape(rows, cols)
    return array


def saveResultsToFiles(sf, df, r):
    plikZapis = open(sf, "w")
    movesMade = []
    if r[0] is None:
        print('-1', file=plikZapis)
    else:
        resultNode = r[0]
        while resultNode.prevNode is not None:
            movesMade.append(resultNode.moveToPrev)
            resultNode = resultNode.prevNode
        print(len(movesMade), file=plikZapis)
        print(''.join(reversed(movesMade)), file=plikZapis)
    plikZapis.close()
    plikDane = open(df, "w")
    if r[0] is None:
        print('-1', file=plikDane)
    else:
        print(len(movesMade), file=plikDane)
        print(r[1], file=plikDane)
        print(r[2], file=plikDane)
        print(r[3], file=plikDane)
        print(f"{r[4]:.3f}", file=plikDane)


# JAK COŚ: WSZYSTKO POWYŻEJ METODY findZeroAndVerify DO USUNIĘCIA POTEM

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("BŁĘDNA ILOŚĆ PARAMETRÓW!")
        print("Przykładowe wywołania programu:")
        print("python main.py bfs RDUL 4x4_01_0001.txt 4x4_01_0001_bfs_rdul_sol.txt 4x4_01_0001_bfs_rdul_stats.txt")
        print("python main.py dfs LUDR 4x4_01_0001.txt 4x4_01_0001_dfs_ludr_sol.txt 4x4_01_0001_dfs_ludr_stats.txt")
        print("python main.py astr manh 4x4_01_0001.txt 4x4_01_0001_astr_manh_sol.txt 4x4_01_0001_astr_manh_stats.txt")
        print("python main.py ALGORYTM STRATEGIA PLIK_WEJŚCIOWY PLIK_WYJŚCIOWY_ROZWIĄZANIE PLIK_WYJŚCIOWY_DODATKOWY")
        print("ALGORYTM - bfs|dfs|astr")
        print("STRATEGIA - permutacja RLDU (z dużych liter) dla bfs|dfs lub - manh|hamm dla astr (z małych liter)")
        print("PLIK_WEJŚCIOWY - nazwa pliku z danymi do pobrania")
        print("PLIK_WYJŚCIOWY_ROZWIĄZANIE - nazwa pliku, w którym zapisze się rozwiązanie")
        print("PLIK_WYJŚCIOWY_DODATKOWY - nazwa pliku, w którym zapisze się dodatkowe informacje")
        sys.exit(1)
    algorithm = sys.argv[1]
    if algorithm not in ["bfs", "dfs", "astr"]:
        print("NIEOBSŁUGIWANA STRATEGIA! bfs|dfs|astr")
        sys.exit(1)
    strategy = sys.argv[2]
    if algorithm == "bfs" or algorithm == "dfs":
        strategy = list(sys.argv[2])
        if set(strategy) != {"L", "R", "D", "U"}:
            print("BŁĘDNA STRATEGIA! permutacja RLDU dla bfs|dfs")
            sys.exit(1)
    elif algorithm == "astr" and strategy not in ("manh", "hamm"):
        print("BŁĘDNA STRATEGIA! manh|hamm dla astr")
        sys.exit(1)
    startBoard = []
    try:
        startBoard = readBoardFromFile()
    except:
        raise ValueError("Wystąpił nieoczekiwany błąd z plikiem wejściowym!")

    # TODO - ASTAR
    # od teraz wywołanie tylko przez terminal, wpisujesz:
    # python main.py bfs RDUL plikwejściowy x x
    # i leci, za bfs i RDUL podstawiasz co chcesz
    # pliki wejściowe są w formacie txt, i wyglądają tak:
    # 4 4
    # 1 2 3 4
    # 5 6 7 8
    # 9 10 11 12
    # 13 14 15 0
    # (1 linijka - rozmiar układanki, pozostałe - układ na planszy)

    startState = Node(startBoard, None, None, 0, findZeroAndVerify(startBoard))
    results = []
    if algorithm == "bfs":
        results = bfs(startState, strategy)
    elif algorithm == "dfs":
        results = dfs(startState, strategy)
    elif algorithm == "astr":
        print("gwiazdka")
        if (strategy == "manh"):
            results = astar(startState, strategy, "manhattan")

        if (strategy == "hamm"):
            results = astar(startState, strategy, "hamming")

    try:
        solutionFile = sys.argv[4]
        dataFile = sys.argv[5]
        saveResultsToFiles(solutionFile, dataFile, results)
    except:
        raise ValueError("Nastąpiły problemy przy zapisie danych do plików!")

    # do usunięcia potem, na potrzeby weryfikacji zapisu na razie
    if algorithm != "astr":
        if results[0] is not None:
            resultNode = results[0]
            movesMade = []
            while resultNode is not startState:
                movesMade.append(resultNode.moveToPrev)
                resultNode = resultNode.prevNode
            print(len(movesMade))
            for r in reversed(movesMade):
                print(r, end="")
            print()
            print("Liczba węzłów odwiedzonych: " + str(results[1]))
            print("Liczba węzłów przetworzonych " + str(results[2]))
            print("Maksymalna głębokość rekursji: " + str(results[3]))
            print("Czas: " + str(results[4]))
