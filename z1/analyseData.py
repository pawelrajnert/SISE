import numpy as np
import matplotlib.pyplot as plt


def readFile():
    dataFile = open("wynikiPietnastka.txt", "r")
    readText = dataFile.read()
    readText = readText.split()
    values = list(map(str, readText))
    array = np.array(values).reshape(7434, 9)
    return array


# Operujemy na zmiennych globalnych w przypadku tworzenia wykresów
data = readFile()
bfsData = data[data[:, 2] == "bfs"]
bfsErrorData = bfsData[bfsData[:, 4] == "-1"]
dfsData = data[data[:, 2] == "dfs"]
dfsErrorData = dfsData[dfsData[:, 4] == "-1"]
astrData = data[data[:, 2] == "astr"]
astrErrorData = astrData[astrData[:, 4] == "-1"]
algorithms = ["BFS", "DFS", "A*"]


def preparePercentagePlot():
    correctBfsSolutionsPercentage = round(100 * (bfsData.shape[0] - bfsErrorData.shape[0]) / bfsData.shape[0], 2)
    correctDfsSolutionsPercentage = round(100 * (dfsData.shape[0] - dfsErrorData.shape[0]) / dfsData.shape[0], 2)
    correctAstrSolutionsPercentage = round(100 * (astrData.shape[0] - astrErrorData.shape[0]) / astrData.shape[0], 2)

    correctSolutions = [correctBfsSolutionsPercentage, correctDfsSolutionsPercentage, correctAstrSolutionsPercentage]
    plt.figure(figsize=(4, 4))
    plt.bar(algorithms, correctSolutions)
    plt.xlabel("Algorytm")
    plt.ylabel("%")
    plt.title("% poprawnych rozwiązań")
    plt.ylim(70, 102)
    plt.tight_layout()
    plt.show()


def prepareDfsAccuracyRegardingMoveOrder():
    permutations = ["drlu", "drul", "ludr", "lurd", "rdlu", "rdul", "uldr", "ulrd"]
    dfsErrors = []
    for i, permutation in enumerate(permutations):
        count = dfsErrorData[dfsErrorData[:,3] == permutation].shape[0]
        percentage = round(100 * count / 413, 2)
        dfsErrors.append(100 - percentage)

    plt.figure(figsize=(4, 4))
    plt.bar(permutations, dfsErrors)
    plt.xlabel("Permutacja")
    plt.ylabel("%")
    plt.title("Algorytm dfs - % poprawnych rozwiązań")
    plt.ylim(75, 85)
    plt.tight_layout()
    plt.show()

def prepareDfsAccuracyRegardingBoardDepth():
    # NIE DZIAŁA NA RAZIE POTEM POPRAWIĘ
    depths = list(range(1,8))
    dfsErrors = []
    for i, depth in enumerate(depths):
        xd = dfsErrorData[dfsErrorData[:, 0] == str(depth)]
        print(xd.shape)
        count = dfsErrorData[dfsErrorData[:, 0] == str(depth)].shape[0]
        print(count)
        percentage = round(100 * count / 413, 2)
        dfsErrors.append(100 - percentage)

    plt.figure(figsize=(4, 4))
    plt.bar(depths, dfsErrors)
    plt.xticks(depths)
    plt.xlabel("Głębokość")
    plt.ylabel("%")
    plt.title("Algorytm dfs - % poprawnych rozwiązań")
    plt.tight_layout()
    plt.show()


preparePercentagePlot()
prepareDfsAccuracyRegardingMoveOrder()
prepareDfsAccuracyRegardingBoardDepth()