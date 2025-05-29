import os

import pandas as pd
import numpy as np
def readData():
    dynData = []
    statData = []
    PATHS_TO_FILES = ["dane/f8/dyn/", "dane/f8/stat/", "dane/f10/dyn/", "dane/f10/stat/"]
    DATA_LIST = [dynData, statData, dynData, statData]
    for pth, dl in zip(PATHS_TO_FILES, DATA_LIST):
        for path in sorted(os.listdir(pth)):
            dl.append(pd.read_csv(pth + path, header=None))
    return np.vstack(statData), np.vstack(dynData)
