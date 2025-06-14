import torch
from scaleData import numpyToTorch
from dataIO import saveData

class NeuralNetwork(torch.nn.Module):

    def __init__(self, hiddenSize, activation):
        super().__init__()
        # ponieważ warstwy wejściowe i wyjściowe składają się z 2 neuronów, wartości te są niemodyfikowalne przez config
        self.inputToHidden = torch.nn.Linear(2, hiddenSize)  # 2 - rozmiar warstwy wejściowej
        self.hiddenToOutput = torch.nn.Linear(hiddenSize, 2)  # 2 - rozmiar warstwy wyjściowej
        if activation == "relu":
            self.activation = torch.nn.ReLU()
        elif activation == "sigmoid":
            self.activation = torch.nn.Sigmoid()
        elif activation == "tanh":
            self.activation = torch.nn.Tanh()
        else:
            raise ValueError("Nieobsługiwana funkcja aktywacji - dozwolone wartości: relu|sigmoid|tanh")

    def forward(self, inputData):
        x = self.inputToHidden(inputData)
        x = self.activation(x)
        x = self.hiddenToOutput(x)
        return x

    def trainNetwork(self, statData, dynData, trainingParams, scaler):
        # Podział danych na dane treningowe i testowe oraz dane wejściowe i wyjściowe
        trainInputData = numpyToTorch(statData, "01")
        trainExpectedData = numpyToTorch(statData, "23")
        testInputData = numpyToTorch(dynData, "01")
        testExpectedData = numpyToTorch(dynData, "23")

        lossFn = torch.nn.MSELoss()
        optimizer = torch.optim.Adam(self.parameters(), lr=trainingParams["lr"])
        maxEpochs = trainingParams["max_epochs"]
        maxErrors = trainingParams["max_errors"]
        errorCounter = 0
        bestError = float("inf")
        bestTestOutput = None
        testMSEValues = []
        trainMSEValues = []
        for epoch in range(maxEpochs):
            # trenowanie sieci na zbiorze treningowym
            self.train()
            optimizer.zero_grad()
            output = self(trainInputData)
            epochLoss = lossFn(output, trainExpectedData)
            epochLoss.backward()
            optimizer.step()
            self.eval()
            # wyliczenie błędu średniokwadratowego na zbiorze treningowym i testowym
            with torch.no_grad():
                trainOutput = self(trainInputData)
                trainLoss = lossFn(trainOutput, trainExpectedData)
                totalTrainLoss = trainLoss.item()
                testOutput = self(testInputData)
                testLoss = lossFn(testOutput, testExpectedData)
                totalTestLoss = testLoss.item()

            if totalTestLoss <= bestError:
                bestError = totalTestLoss
                bestTestOutput = testOutput
            else:
                errorCounter += 1

            if errorCounter == maxErrors:
                print(f"Zakończono trenowanie sieci z uwagi na osiągnięcie wartości maksymalnej {trainingParams['max_errors']} błędów podczas procesu nauki.")
                print(f"Ostatni wynik spełniający warunek: epoch: {epoch + 1}, trainLoss: {totalTrainLoss:.10f}, testLoss: {totalTestLoss:.10f}")
                break
            testMSEValues.append(totalTestLoss)
            trainMSEValues.append(totalTrainLoss)
        saveData(testMSEValues, trainMSEValues, bestTestOutput, scaler)
