import numpy as np
def readFile():
    dataFile = open("wynikiPietnastka.txt", "r")
    readText = dataFile.read()
    readText = readText.split()
    values = list(map(str, readText))
    array = np.array(values).reshape(7434, 9)
    return array

data = readFile()