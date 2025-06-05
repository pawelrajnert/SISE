import json
import pandas as pd
import matplotlib.pyplot as plt
from dataIO import readData
import numpy as np
def calculateDifference(output, realData):
    print(output)
    diff = []
    for o, r in zip(output, realData):
        distance = np.linalg.norm(o - r)
        diff.append(distance)
    diff.sort()
    return diff

config = json.load(open('config.json'))
relu_mse_test = "wyniki/relu-" + config['MSEtestFile']
relu_mse_train = "wyniki/relu-" + config['MSEtrainFile']
relu_output = "wyniki/relu-" + config['outputFile']
tanh_mse_test = "wyniki/tanh-" + config['MSEtestFile']
tanh_mse_train = "wyniki/tanh-" + config['MSEtrainFile']
tanh_output = "wyniki/tanh-" + config['outputFile']
sigmoid_mse_test = "wyniki/sigmoid-" + config['MSEtestFile']
sigmoid_mse_train = "wyniki/sigmoid-" + config['MSEtrainFile']
sigmoid_output = "wyniki/sigmoid-" + config['outputFile']

_, dynData = readData()

relu_data = np.array(pd.read_csv(relu_output, header=None))
sigmoid_data = np.array(pd.read_csv(sigmoid_output, header=None))
tanh_data = np.array(pd.read_csv(tanh_output, header=None))
robot_data = dynData[:, :2]

relu_diffs = calculateDifference(relu_data, dynData[:, :2])
sigmoid_diffs = calculateDifference(sigmoid_data, dynData[:, 2:])
tanh_diffs = calculateDifference(tanh_data, dynData[:, 2:])
robot_diffs = calculateDifference(robot_data, dynData[:, 2:])
relu_y = np.linspace(0, 1, len(relu_diffs))
sigmoid_y = np.linspace(0, 1, len(sigmoid_diffs))
tanh_y = np.linspace(0, 1, len(tanh_diffs))
robot_y = np.linspace(0, 1, len(robot_diffs))
plt.figure(figsize=(12, 8))
plt.plot(relu_diffs, relu_y, label="relu", color="blue")
plt.plot(sigmoid_diffs, sigmoid_y, label="sigmoid", color="red")
plt.plot(tanh_diffs, tanh_y, label="tanh", color="green")
plt.plot(robot_diffs, robot_y, label="robot", color="black")
plt.legend()
plt.show()



x = relu_data[:, 0]
y = relu_data[:, 1]
x1 = dynData[:, 0]
y1 = dynData[:, 1]
x2 = dynData[:, 2]
y2 = dynData[:, 3]

plt.figure(figsize=(14, 10))
plt.scatter(x1, y1, color='red', label='Zmierzone', alpha=0.4, s=15)
plt.scatter(x, y, color='blue', label='Skorygowane', alpha=0.7, s=15)
plt.scatter(x2, y2, color='green', label='Rzeczywiste', alpha=1.0, s=25)

plt.xlabel("X [mm]")
plt.ylabel("Y [mm]")
plt.title("Wyniki pomiarów dynamicznych: rzeczywiste vs skorygowane vs zmierzone")
plt.legend()
plt.grid(True)
plt.show()