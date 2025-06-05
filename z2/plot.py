import json
import pandas as pd
import matplotlib.pyplot as plt
from dataIO import readData
import numpy as np
from scaleData import scaleData
def drawPlots():
    def calculateDifference(output, realData):
        print(output)
        diff = []
        for o, r in zip(output, realData):
            distance = np.linalg.norm(o - r)
            diff.append(distance)
        diff.sort()
        return diff

    config = json.load(open('config.json'))
    relu_output = "wyniki/relu-" + config['outputFile']
    tanh_output = "wyniki/tanh-" + config['outputFile']
    sigmoid_output = "wyniki/sigmoid-" + config['outputFile']

    statData, dynData = readData()

    relu_data = np.array(pd.read_csv(relu_output, header=None))
    sigmoid_data = np.array(pd.read_csv(sigmoid_output, header=None))
    tanh_data = np.array(pd.read_csv(tanh_output, header=None))
    relu_train = pd.read_csv(f"wyniki/relu-{config['MSEtrainFile']}", header=None).values.flatten()
    sigmoid_train = pd.read_csv(f"wyniki/sigmoid-{config['MSEtrainFile']}", header=None).values.flatten()
    tanh_train = pd.read_csv(f"wyniki/tanh-{config['MSEtrainFile']}", header=None).values.flatten()
    relu_test = pd.read_csv(f"wyniki/relu-{config['MSEtestFile']}", header=None).values.flatten()
    sigmoid_test = pd.read_csv(f"wyniki/sigmoid-{config['MSEtestFile']}", header=None).values.flatten()
    tanh_test = pd.read_csv(f"wyniki/tanh-{config['MSEtestFile']}", header=None).values.flatten()
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



    x = tanh_data[:, 0]
    y = tanh_data[:, 1]
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


    epochs = range(1, len(relu_train) + 1)

    plt.figure(figsize=(12, 8))
    plt.plot(epochs, relu_train, label='ReLU', color='blue', linewidth=2)
    plt.plot(epochs, sigmoid_train, label='Sigmoid', color='red', linewidth=2)
    plt.plot(epochs, tanh_train, label='Tanh', color='green', linewidth=2)

    plt.xlabel('Epoka')
    plt.ylabel('Błąd MSE')
    plt.title('Błąd średniokwadratowy na zbiorze uczącym')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Opcjonalne skalowanie osi Y (ucięcie górnych wartości z początkowych epok)
    # Można odkomentować poniższą linię jeśli wartości z początkowych epok są bardzo wysokie
    plt.ylim(-0.02, 0.5)

    # Opcjonalna skala logarytmiczna dla osi Y
    # plt.yscale('log')

    plt.tight_layout()
    plt.show()

    scaledStatData, scaledDynData, usedScaler = scaleData(statData, dynData, config['scalerType'])

    measured_scaled = scaledDynData[:, :2]
    real_scaled = scaledDynData[:, 2:]
    reference_mse = np.mean((measured_scaled - real_scaled) ** 2)

    plt.figure(figsize=(12, 8))
    plt.plot(epochs, relu_test, label='ReLU', color='blue', linewidth=2)
    plt.plot(epochs, sigmoid_test, label='Sigmoid', color='red', linewidth=2)
    plt.plot(epochs, tanh_test, label='Tanh', color='green', linewidth=2)

    # Dodanie poziomej linii odniesienia
    plt.axhline(y=reference_mse, color='black', linestyle='--', linewidth=2,
                label=f'Błąd zmierzonych wartości (MSE={reference_mse:.6f})')

    plt.xlabel('Epoka')
    plt.ylabel('Błąd MSE')
    plt.title('Błąd średniokwadratowy na zbiorze testowym')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Dopasowanie skali Y do pierwszego wykresu (jeśli potrzeba)
    # plt.ylim(bottom=0, top=max_y_value_from_first_plot)

    plt.tight_layout()
    plt.show()

