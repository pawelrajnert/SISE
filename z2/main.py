from dataIO import readData
from scaleData import scaleData
import json
from neuralNetwork import *
# załadowanie configu
try:
    config = json.load(open('config.json'))
    activation = config['activation']
    scalerType = config['scalerType']
    hiddenSize = config['hiddenSize']
    lr = config['lr']
    max_epochs = config['max_epochs']
    max_errors = config['max_errors']

except FileNotFoundError:
    raise ValueError("Nie można załadować pliku z configiem; upewnij się, że plik config.json znajduje się w katalogu.")
except KeyError:
    raise ValueError("Nie udało się wczytać pliku z configiem - upewnij się, że etykiety pól prawidłowo się nazywają.")


# załadowanie i skalowanie danych
statData, dynData = readData()
scaledStatData, scaledDynData, usedScaler = scaleData(statData, dynData, scalerType)

net = NeuralNetwork(hiddenSize, activation)
trainingParams = {'lr': lr, 'max_epochs': max_epochs, 'max_errors': max_errors}
print("Rozpoczynam trenowanie sieci...")
net.trainNetwork(scaledStatData, scaledDynData, trainingParams, usedScaler)
