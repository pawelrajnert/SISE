from readData import readData
from scaleData import *
import numpy as np
import json
from neuralNetwork import *

# załadowanie configu
config = json.load(open('config.json'))
activation = config['activation']
scalerType = config['scalerType']
hiddenSize = config['hiddenSize']

# załadowanie i skalowanie danych
statData, dynData = readData()
scaledStatData, scaledDynData, usedScaler = scaleData(statData, dynData, scalerType)

# podział danych na wejście do sieci (zmierzona wartość) i oczekiwany wynik (rzeczywiste położenie)
trainInputData = numpyToTorch(scaledStatData, "01")
trainExpectedData = numpyToTorch(scaledStatData, "23")

# wstępne działania na sieci
net = NeuralNetwork(hiddenSize, activation)
result = net.forward(trainInputData)
print(result)

# sprawdzanie odwrotności skalowania - do wywalenia później
reverseDynData = reverseScale(scaledDynData, usedScaler)
reverseStatData = reverseScale(scaledStatData, usedScaler)
if np.allclose(statData, reverseStatData): print("stat")
if np.allclose(dynData, reverseDynData): print("dyn")
