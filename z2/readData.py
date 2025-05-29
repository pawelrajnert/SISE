import os
import pandas as pd
import numpy as np


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
