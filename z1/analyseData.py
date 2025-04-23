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
dfsData = data[data[:, 2] == "dfs"]
dfsErrorData = dfsData[dfsData[:, 4] == "-1"]
astrData = data[data[:, 2] == "astr"]
algorithms = ["BFS", "DFS", "A*"]
dfsCorrectSolved = dfsData[dfsData[:, 4] != "-1"]

def plot1():
    depths = list(range(1, 8))

    bfsPrint = []
    dfsPrint = []
    astrPrint = []

    for depth in depths:
        bfsRows = bfsData[bfsData[:, 0] == str(depth)]
        dfsRows = dfsCorrectSolved[dfsCorrectSolved[:, 0] == str(depth)]
        # tu zmienic po 1 zeby bylo na dfsData
        #dfsRows = dfsData[dfsData[:, 0] == str(depth)]
        astrRows = astrData[astrData[:, 0] == str(depth)]

        bfsAvg = np.mean(bfsRows[:,4].astype(float))
        dfsAvg = np.mean(dfsRows[:, 4].astype(float))
        astrAvg = np.mean(astrRows[:,4].astype(float))
        print(dfsRows.shape)
        bfsPrint.append(bfsAvg)
        dfsPrint.append(dfsAvg)
        astrPrint.append(astrAvg)

    x = np.arange(len(depths))

    plt.bar(x - 0.3, bfsPrint, width=0.3, label="BFS", color="C0")
    plt.bar(x, dfsPrint, width=0.3, label="DFS", color="C1")
    plt.bar(x + 0.3, astrPrint, width=0.3, label="A*", color="C2")

    #plt.yscale("log")
    plt.xticks(x, depths)
    plt.xlabel("Głębokość")
    plt.ylabel("Średnia arytmetyczna długości rozwiązania")
    plt.legend()
    plt.tight_layout()
    print(astrPrint)
    print(bfsPrint)
    print(dfsPrint)
    plt.show()

def plot2ASTR():
    depths = list(range(1, 8))




plot1()
plot2ASTR()
#preparePercentagePlot()
#prepareDfsAccuracyRegardingMoveOrder()
#prepareDfsAccuracyRegardingBoardDepth()