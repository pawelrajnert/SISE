import sys

from Node import Node
from bfs import bfs
from dfs import dfs
from astr import *


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
    moves = []
    if r[0] is None:
        print('-1', file=plikZapis, end='')

    else:
        resultNode = r[0]

        while resultNode.prevNode is not None:
            moves.append(resultNode.moveToPrev)
            resultNode = resultNode.prevNode

        print(len(moves), file=plikZapis)
        print(''.join(reversed(moves)), file=plikZapis, end='')

    plikZapis.close()
    plikDane = open(df, "w")

    if r[0] is None:
        print('-1', file=plikDane)

    else:
        print(len(moves), file=plikDane)

    print(r[1], file=plikDane)
    print(r[2], file=plikDane)
    print(r[3], file=plikDane)
    print(f"{r[4]:.3f}", file=plikDane, end='')
    plikDane.close()


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

    startState = Node(startBoard, None, None, 0, findZeroAndVerify(startBoard))
    results = []
    if algorithm == "bfs":
        results = bfs(startState, strategy)

    elif algorithm == "dfs":
        results = dfs(startState, strategy)

    elif algorithm == "astr":
        results = astar(startState, strategy)

    try:
        solutionFile = sys.argv[4]
        dataFile = sys.argv[5]
        saveResultsToFiles(solutionFile, dataFile, results)

    except:
        raise ValueError("Nastąpiły problemy przy zapisie danych do plików!")