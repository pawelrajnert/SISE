import numpy as np

def prepareGoalBoard(startNode):
    rows = startNode.state.shape[0]
    cols = startNode.state.shape[1]
    numbers = list(range(1,rows*cols)) + [0]
    return np.array(numbers).reshape(rows,cols)