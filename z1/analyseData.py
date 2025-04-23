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

    permutations = ["rdlu", "rdul", "drul", "drlu", "ludr", "lurd", "uldr", "ulrd"]

    bfsPrint = []
    dfsPrint = []
    astrPrint = []

    astrManhattan = []
    astrHamming = []

    bfsPermutations = []
    dfsPermutations = []

    for depth in depths:
        bfsRows = bfsData[bfsData[:, 0] == str(depth)]
        dfsRows = dfsCorrectSolved[dfsCorrectSolved[:, 0] == str(depth)]
        # tu zmienic po 1 zeby bylo na dfsData
        # dfsRows = dfsData[dfsData[:, 0] == str(depth)]
        astrRows = astrData[astrData[:, 0] == str(depth)]

        bfsAvg = np.mean(bfsRows[:, 4].astype(float))
        dfsAvg = np.mean(dfsRows[:, 4].astype(float))
        astrAvg = np.mean(astrRows[:, 4].astype(float))
        bfsPrint.append(bfsAvg)
        dfsPrint.append(dfsAvg)
        astrPrint.append(astrAvg)

        # wykres do a*
        astrHamm = astrRows[astrRows[:, 3] == "hamm"]
        astrManh = astrRows[astrRows[:, 3] == "manh"]
        astrHammAvg = np.mean(astrHamm[:, 4].astype(float))
        astrManhAvg = np.mean(astrManh[:, 4].astype(float))
        astrHamming.append(astrHammAvg)
        astrManhattan.append(astrManhAvg)

        # wykres do bfs i dfs
        for i, permutation in enumerate(permutations):
            bfsRowPermutation = bfsRows[bfsRows[:, 3] == permutation]
            bfsPermutationAvg = np.mean(bfsRowPermutation[:, 4].astype(float))
            bfsPermutations.append(bfsPermutationAvg)

            dfsRowPermutation = dfsRows[dfsRows[:, 3] == permutation]
            dfsPermutationAvg = np.mean(dfsRowPermutation[:, 4].astype(float))
            dfsPermutations.append(dfsPermutationAvg)

    bfsPermutations = np.array(bfsPermutations).reshape(7, 8)
    bfsPermutations = np.transpose(bfsPermutations)
    dfsPermutations = np.array(dfsPermutations).reshape(7, 8)
    dfsPermutations = np.transpose(dfsPermutations)

    x = np.arange(len(depths))
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)

    plt.bar(x - 0.3, bfsPrint, width=0.3, label="BFS", color="C0")
    plt.bar(x, dfsPrint, width=0.3, label="DFS", color="C1")
    plt.bar(x + 0.3, astrPrint, width=0.3, label="A*", color="C2")

    # plt.yscale("log")

    plt.xticks(x, depths)
    plt.title("Ogółem")
    plt.xlabel("Głębokość")
    plt.ylabel("Średnia arytmetyczna długości rozwiązania")
    plt.legend()

    plt.subplot(2, 2, 2)

    plt.bar(x - 0.15, astrHamming, width=0.3, label="Hamming", color="C0")
    plt.bar(x + 0.15, astrManhattan, width=0.3, label="Manhattan", color="C1")
    plt.xticks(x, depths)
    plt.xlabel("Głębokość")
    plt.ylabel("Średnia arytmetyczna długości rozwiązania")
    plt.title("A*")
    plt.legend()

    plt.subplot(2, 2, 3)

    for i in range(8):
        plt.bar(x - 0.35 + i * 0.1, bfsPermutations[i], width=0.1, label=permutations[i].upper(), color=f"C{i}")
    plt.xticks(x, depths)
    plt.legend()
    plt.ylabel("Średnia arytmetyczna długości rozwiązania")
    plt.xlabel("Głębokość")
    plt.title("BFS")

    plt.subplot(2, 2, 4)

    for i in range(8):
        plt.bar(x - 0.35 + i * 0.1, dfsPermutations[i], width=0.1, label=permutations[i].upper(), color=f"C{i}")
    plt.xticks(x, depths)
    plt.ylabel("Średnia arytmetyczna długości rozwiązania")
    plt.xlabel("Głębokość")
    plt.title("DFS")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot2():
    depths = list(range(1, 8))

    permutations = ["rdlu", "rdul", "drul", "drlu", "ludr", "lurd", "uldr", "ulrd"]

    bfsPrint = []
    dfsPrint = []
    astrPrint = []

    astrManhattan = []
    astrHamming = []

    bfsPermutations = []
    dfsPermutations = []

    for depth in depths:
        bfsRows = bfsData[bfsData[:, 0] == str(depth)]
        dfsRows = dfsData[dfsData[:, 0] == str(depth)]
        astrRows = astrData[astrData[:, 0] == str(depth)]

        bfsAvg = np.mean(bfsRows[:, 5].astype(float))
        dfsAvg = np.mean(dfsRows[:, 5].astype(float))
        astrAvg = np.mean(astrRows[:, 5].astype(float))
        bfsPrint.append(bfsAvg)
        dfsPrint.append(dfsAvg)
        astrPrint.append(astrAvg)

        # wykres do a*
        astrHamm = astrRows[astrRows[:, 3] == "hamm"]
        astrManh = astrRows[astrRows[:, 3] == "manh"]
        astrHammAvg = np.mean(astrHamm[:, 5].astype(float))
        astrManhAvg = np.mean(astrManh[:, 5].astype(float))
        astrHamming.append(astrHammAvg)
        astrManhattan.append(astrManhAvg)

        # wykres do bfs i dfs
        for i, permutation in enumerate(permutations):
            bfsRowPermutation = bfsRows[bfsRows[:, 3] == permutation]
            bfsPermutationAvg = np.mean(bfsRowPermutation[:, 5].astype(float))
            bfsPermutations.append(bfsPermutationAvg)

            dfsRowPermutation = dfsRows[dfsRows[:, 3] == permutation]
            dfsPermutationAvg = np.mean(dfsRowPermutation[:, 5].astype(float))
            dfsPermutations.append(dfsPermutationAvg)

    bfsPermutations = np.array(bfsPermutations).reshape(7, 8)
    bfsPermutations = np.transpose(bfsPermutations)
    dfsPermutations = np.array(dfsPermutations).reshape(7, 8)
    dfsPermutations = np.transpose(dfsPermutations)

    x = np.arange(len(depths))
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)

    plt.bar(x - 0.3, bfsPrint, width=0.3, label="BFS", color="C0")
    plt.bar(x, dfsPrint, width=0.3, label="DFS", color="C1")
    plt.bar(x + 0.3, astrPrint, width=0.3, label="A*", color="C2")

    plt.xticks(x, depths)
    plt.yscale("log")
    plt.yticks([1,10,100,1000,10000,100000],[1,10,100,1000,10000,100000])
    plt.ylim(1,300000)
    plt.title("Ogółem")
    plt.xlabel("Głębokość")
    plt.ylabel("Liczba stanów odwiedzonych")
    plt.legend()

    plt.subplot(2, 2, 2)

    plt.bar(x - 0.15, astrHamming, width=0.3, label="Hamming", color="C0")
    plt.bar(x + 0.15, astrManhattan, width=0.3, label="Manhattan", color="C1")
    plt.xticks(x, depths)
    plt.yticks([0, 5, 10, 15, 20, 25], [0, 5, 10, 15, 20, 25])
    plt.xlabel("Głębokość")
    plt.ylabel("Liczba stanów odwiedzonych")
    plt.title("A*")
    plt.legend()

    plt.subplot(2, 2, 3)

    for i in range(8):
        plt.bar(x - 0.35 + i * 0.1, bfsPermutations[i], width=0.1, label=permutations[i].upper(), color=f"C{i}")
    plt.xticks(x, depths)
    plt.yscale("log")
    plt.yticks([1, 10, 100, 1000], [1, 10, 100, 1000])
    plt.legend()
    plt.ylabel("Liczba stanów odwiedzonych")
    plt.xlabel("Głębokość")
    plt.title("BFS")

    plt.subplot(2, 2, 4)

    for i in range(8):
        plt.bar(x - 0.35 + i * 0.1, dfsPermutations[i], width=0.1, label=permutations[i].upper(), color=f"C{i}")
    plt.xticks(x, depths)
    plt.yscale("log")
    plt.yticks([1, 10, 100, 1000, 10000, 100000], [1, 10, 100, 1000, 10000, 100000])
    plt.ylim(1,300000)
    plt.ylabel("Liczba stanów odwiedzonych")
    plt.xlabel("Głębokość")
    plt.title("DFS")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot3():
    depths = list(range(1, 8))

    permutations = ["rdlu", "rdul", "drul", "drlu", "ludr", "lurd", "uldr", "ulrd"]

    bfsPrint = []
    dfsPrint = []
    astrPrint = []

    astrManhattan = []
    astrHamming = []

    bfsPermutations = []
    dfsPermutations = []

    for depth in depths:
        bfsRows = bfsData[bfsData[:, 0] == str(depth)]
        dfsRows = dfsData[dfsData[:, 0] == str(depth)]
        astrRows = astrData[astrData[:, 0] == str(depth)]

        bfsAvg = np.mean(bfsRows[:, 6].astype(float))
        dfsAvg = np.mean(dfsRows[:, 6].astype(float))
        astrAvg = np.mean(astrRows[:, 6].astype(float))
        bfsPrint.append(bfsAvg)
        dfsPrint.append(dfsAvg)
        astrPrint.append(astrAvg)

        # wykres do a*
        astrHamm = astrRows[astrRows[:, 3] == "hamm"]
        astrManh = astrRows[astrRows[:, 3] == "manh"]
        astrHammAvg = np.mean(astrHamm[:, 6].astype(float))
        astrManhAvg = np.mean(astrManh[:, 6].astype(float))
        astrHamming.append(astrHammAvg)
        astrManhattan.append(astrManhAvg)

        # wykres do bfs i dfs
        for i, permutation in enumerate(permutations):
            bfsRowPermutation = bfsRows[bfsRows[:, 3] == permutation]
            bfsPermutationAvg = np.mean(bfsRowPermutation[:, 6].astype(float))
            bfsPermutations.append(bfsPermutationAvg)

            dfsRowPermutation = dfsRows[dfsRows[:, 3] == permutation]
            dfsPermutationAvg = np.mean(dfsRowPermutation[:, 6].astype(float))
            dfsPermutations.append(dfsPermutationAvg)

    bfsPermutations = np.array(bfsPermutations).reshape(7, 8)
    bfsPermutations = np.transpose(bfsPermutations)
    dfsPermutations = np.array(dfsPermutations).reshape(7, 8)
    dfsPermutations = np.transpose(dfsPermutations)

    x = np.arange(len(depths))
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)

    plt.bar(x - 0.3, bfsPrint, width=0.3, label="BFS", color="C0")
    plt.bar(x, dfsPrint, width=0.3, label="DFS", color="C1")
    plt.bar(x + 0.3, astrPrint, width=0.3, label="A*", color="C2")

    plt.xticks(x, depths)
    plt.yscale("log")
    plt.yticks([1,10,100,1000,10000,100000],[1,10,100,1000,10000,100000])
    plt.ylim(1,300000)
    plt.title("Ogółem")
    plt.xlabel("Głębokość")
    plt.ylabel("Liczba stanów przetworzonych")
    plt.legend()

    plt.subplot(2, 2, 2)

    plt.bar(x - 0.15, astrHamming, width=0.3, label="Hamming", color="C0")
    plt.bar(x + 0.15, astrManhattan, width=0.3, label="Manhattan", color="C1")
    plt.xticks(x, depths)
    plt.yticks([0, 5, 10, 15, 20, 25], [0, 5, 10, 15, 20, 25])
    plt.xlabel("Głębokość")
    plt.ylabel("Liczba stanów przetworzonych")
    plt.title("A*")
    plt.legend()

    plt.subplot(2, 2, 3)

    for i in range(8):
        plt.bar(x - 0.35 + i * 0.1, bfsPermutations[i], width=0.1, label=permutations[i].upper(), color=f"C{i}")
    plt.xticks(x, depths)
    plt.yscale("log")
    plt.yticks([1, 10, 100, 1000], [1, 10, 100, 1000])
    plt.legend()
    plt.ylabel("Liczba stanów przetworzonych")
    plt.xlabel("Głębokość")
    plt.title("BFS")

    plt.subplot(2, 2, 4)

    for i in range(8):
        plt.bar(x - 0.35 + i * 0.1, dfsPermutations[i], width=0.1, label=permutations[i].upper(), color=f"C{i}")
    plt.xticks(x, depths)
    plt.yscale("log")
    plt.yticks([1, 10, 100, 1000, 10000, 100000], [1, 10, 100, 1000, 10000, 100000])
    plt.ylim(1,300000)
    plt.ylabel("Liczba stanów przetworzonych")
    plt.xlabel("Głębokość")
    plt.title("DFS")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot4():
    depths = list(range(1, 8))

    permutations = ["rdlu", "rdul", "drul", "drlu", "ludr", "lurd", "uldr", "ulrd"]

    bfsPrint = []
    dfsPrint = []
    astrPrint = []

    astrManhattan = []
    astrHamming = []

    bfsPermutations = []
    dfsPermutations = []

    for depth in depths:
        bfsRows = bfsData[bfsData[:, 0] == str(depth)]
        dfsRows = dfsData[dfsData[:, 0] == str(depth)]
        astrRows = astrData[astrData[:, 0] == str(depth)]

        bfsAvg = np.mean(bfsRows[:, 7].astype(float))
        dfsAvg = np.mean(dfsRows[:, 7].astype(float))
        astrAvg = np.mean(astrRows[:, 7].astype(float))
        bfsPrint.append(bfsAvg)
        dfsPrint.append(dfsAvg)
        astrPrint.append(astrAvg)

        # wykres do a*
        astrHamm = astrRows[astrRows[:, 3] == "hamm"]
        astrManh = astrRows[astrRows[:, 3] == "manh"]
        astrHammAvg = np.mean(astrHamm[:, 7].astype(float))
        astrManhAvg = np.mean(astrManh[:, 7].astype(float))
        astrHamming.append(astrHammAvg)
        astrManhattan.append(astrManhAvg)

        # wykres do bfs i dfs
        for i, permutation in enumerate(permutations):
            bfsRowPermutation = bfsRows[bfsRows[:, 3] == permutation]
            bfsPermutationAvg = np.mean(bfsRowPermutation[:, 7].astype(float))
            bfsPermutations.append(bfsPermutationAvg)

            dfsRowPermutation = dfsRows[dfsRows[:, 3] == permutation]
            dfsPermutationAvg = np.mean(dfsRowPermutation[:, 7].astype(float))
            dfsPermutations.append(dfsPermutationAvg)

    bfsPermutations = np.array(bfsPermutations).reshape(7, 8)
    bfsPermutations = np.transpose(bfsPermutations)
    dfsPermutations = np.array(dfsPermutations).reshape(7, 8)
    dfsPermutations = np.transpose(dfsPermutations)

    x = np.arange(len(depths))
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)

    plt.bar(x - 0.3, bfsPrint, width=0.3, label="BFS", color="C0")
    plt.bar(x, dfsPrint, width=0.3, label="DFS", color="C1")
    plt.bar(x + 0.3, astrPrint, width=0.3, label="A*", color="C2")

    plt.xticks(x, depths)
    plt.title("Ogółem")
    plt.xlabel("Głębokość")
    plt.ylabel("Średnia osiągnięta maksymalna głębokość rekursji")
    plt.legend()

    plt.subplot(2, 2, 2)

    plt.bar(x - 0.15, astrHamming, width=0.3, label="Hamming", color="C0")
    plt.bar(x + 0.15, astrManhattan, width=0.3, label="Manhattan", color="C1")
    plt.xticks(x, depths)
    plt.xlabel("Głębokość")
    plt.ylabel("Średnia osiągnięta maksymalna głębokość rekursji")
    plt.title("A*")
    plt.legend()

    plt.subplot(2, 2, 3)

    for i in range(8):
        plt.bar(x - 0.35 + i * 0.1, bfsPermutations[i], width=0.1, label=permutations[i].upper(), color=f"C{i}")
    plt.xticks(x, depths)
    plt.legend()
    plt.ylabel("Średnia osiągnięta maksymalna głębokość rekursji")
    plt.xlabel("Głębokość")
    plt.title("BFS")

    plt.subplot(2, 2, 4)

    for i in range(8):
        plt.bar(x - 0.35 + i * 0.1, dfsPermutations[i], width=0.1, label=permutations[i].upper(), color=f"C{i}")
    plt.xticks(x, depths)
    plt.ylabel("Średnia osiągnięta maksymalna głębokość rekursji")
    plt.xlabel("Głębokość")
    plt.title("DFS")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot5():
    depths = list(range(1, 8))

    permutations = ["rdlu", "rdul", "drul", "drlu", "ludr", "lurd", "uldr", "ulrd"]

    bfsPrint = []
    dfsPrint = []
    astrPrint = []

    astrManhattan = []
    astrHamming = []

    bfsPermutations = []
    dfsPermutations = []

    for depth in depths:
        bfsRows = bfsData[bfsData[:, 0] == str(depth)]
        dfsRows = dfsData[dfsData[:, 0] == str(depth)]
        astrRows = astrData[astrData[:, 0] == str(depth)]

        bfsAvg = np.mean(bfsRows[:, 8].astype(float))
        dfsAvg = np.mean(dfsRows[:, 8].astype(float))
        astrAvg = np.mean(astrRows[:, 8].astype(float))
        bfsPrint.append(bfsAvg)
        dfsPrint.append(dfsAvg)
        astrPrint.append(astrAvg)

        # wykres do a*
        astrHamm = astrRows[astrRows[:, 3] == "hamm"]
        astrManh = astrRows[astrRows[:, 3] == "manh"]
        astrHammAvg = np.mean(astrHamm[:, 8].astype(float))
        astrManhAvg = np.mean(astrManh[:, 8].astype(float))
        astrHamming.append(astrHammAvg)
        astrManhattan.append(astrManhAvg)

        # wykres do bfs i dfs
        for i, permutation in enumerate(permutations):
            bfsRowPermutation = bfsRows[bfsRows[:, 3] == permutation]
            bfsPermutationAvg = np.mean(bfsRowPermutation[:, 8].astype(float))
            bfsPermutations.append(bfsPermutationAvg)

            dfsRowPermutation = dfsRows[dfsRows[:, 3] == permutation]
            dfsPermutationAvg = np.mean(dfsRowPermutation[:, 8].astype(float))
            dfsPermutations.append(dfsPermutationAvg)

    bfsPermutations = np.array(bfsPermutations).reshape(7, 8)
    bfsPermutations = np.transpose(bfsPermutations)
    dfsPermutations = np.array(dfsPermutations).reshape(7, 8)
    dfsPermutations = np.transpose(dfsPermutations)

    x = np.arange(len(depths))
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)

    plt.bar(x - 0.3, bfsPrint, width=0.3, label="BFS", color="C0")
    plt.bar(x, dfsPrint, width=0.3, label="DFS", color="C1")
    plt.bar(x + 0.3, astrPrint, width=0.3, label="A*", color="C2")

    plt.xticks(x, depths)
    plt.yscale("log")
    plt.yticks([0.0001,0.001,0.01,0.1,1,10],[0.0001,0.001,0.01,0.1,1,10])
    plt.ylim(0.0001,10)
    plt.title("Ogółem")
    plt.xlabel("Głębokość")
    plt.ylabel("Średni czas trwania procesu obliczeniowego")
    plt.legend()

    plt.subplot(2, 2, 2)

    plt.bar(x - 0.15, astrHamming, width=0.3, label="Hamming", color="C0")
    plt.bar(x + 0.15, astrManhattan, width=0.3, label="Manhattan", color="C1")
    plt.xticks(x, depths)
    plt.yscale("log")
    plt.yticks([0.0001, 0.001, 0.01, 0.1], [0.0001, 0.001, 0.01, 0.1])
    plt.ylim(0.0001, 0.1)
    plt.xlabel("Głębokość")
    plt.ylabel("Średni czas trwania procesu obliczeniowego")
    plt.title("A*")
    plt.legend()

    plt.subplot(2, 2, 3)

    for i in range(8):
        plt.bar(x - 0.35 + i * 0.1, bfsPermutations[i], width=0.1, label=permutations[i].upper(), color=f"C{i}")
    plt.xticks(x, depths)

    plt.legend()
    plt.ylabel("Średni czas trwania procesu obliczeniowego")
    plt.xlabel("Głębokość")
    plt.title("BFS")

    plt.subplot(2, 2, 4)

    for i in range(8):
        plt.bar(x - 0.35 + i * 0.1, dfsPermutations[i], width=0.1, label=permutations[i].upper(), color=f"C{i}")
    plt.xticks(x, depths)
    plt.yscale("log")
    plt.yticks([0.0001, 0.001, 0.01, 0.1, 1, 10], [0.0001, 0.001, 0.01, 0.1, 1, 10])
    plt.ylim(0.0001, 10)
    plt.ylabel("Średni czas trwania procesu obliczeniowego")
    plt.xlabel("Głębokość")
    plt.title("DFS")
    plt.legend()
    plt.tight_layout()
    plt.show()

plot1()
plot2()
plot3()
plot4()
plot5()