import os
import pandas as pd
import numpy as np
import json
from scaleData import reverseScale

# Zgodnie z 2 akapitem opisu części badawczej, tworzymy dwa zbiory, zawierające 4 kolumny:
# - zbiór do uczenia sieci (dane z plików z katalogów "stat")
# - zbiór do testowania sieci (dane z plików z katalogów "dyn")
def readData():
    dynData = []
    statData = []
    PATHS_TO_FILES = ["dane/f8/dyn/", "dane/f8/stat/", "dane/f10/dyn/", "dane/f10/stat/"]
    DATA_LIST = [dynData, statData, dynData, statData]
    for pth, dl in zip(PATHS_TO_FILES, DATA_LIST):
        for path in sorted(os.listdir(pth)):
            dl.append(pd.read_csv(pth + path, header=None))
    return np.vstack(statData), np.vstack(dynData)


def saveData(testMSEValues, trainMSEValues, bestOutput, scaler):

    config = json.load(open('config.json'))
    os.makedirs("wyniki", exist_ok=True)
    if config["saveToFile"] == "YES":
        data = pd.DataFrame(testMSEValues)
        data.to_csv(f"wyniki/{config["activation"]}-{config["MSEtestFile"]}", index=False, header=False)
        data = pd.DataFrame(trainMSEValues)
        data.to_csv(f"wyniki/{config["activation"]}-{config["MSEtrainFile"]}", index=False, header=False)
        fillDataWithZeros = np.zeros((bestOutput.shape[0], 4))
        fillDataWithZeros[:, 2:] = bestOutput
        scaledData = reverseScale(fillDataWithZeros, scaler)
        data = pd.DataFrame(scaledData[:, 2:])
        data.to_csv(f"wyniki/{config["activation"]}-{config["outputFile"]}", index=False, header=False)
        print("Zapisano dane do plików w katalogu wyniki")
