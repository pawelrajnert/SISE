import torch
from scaleData import numpyToTorch


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


def trainNetwork(net, statData, dynData, trainingParams):
    # Podział danych na dane treningowe i testowe oraz dane wejściowe i wyjściowe
    trainInputData = numpyToTorch(statData, "01")
    trainExpectedData = numpyToTorch(statData, "23")
    testInputData = numpyToTorch(dynData, "01")
    testExpectedData = numpyToTorch(dynData, "23")

    lossFn = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=trainingParams["lr"])
    maxEpochs = trainingParams["max_epochs"]
    maxErrors = trainingParams["max_errors"]
    errorCounter = 0
    bestError = float("inf")

    for epoch in range(maxEpochs):
        # trenowanie sieci na zbiorze treningowym
        net.train()
        optimizer.zero_grad()
        output = net(trainInputData)
        loss = lossFn(output, trainExpectedData)
        loss.backward()
        optimizer.step()
        net.eval()
        # wyliczenie błędu średniokwadratowego na zbiorze treningowym i testowym
        with torch.no_grad():
            trainOutput = net(trainInputData)
            loss = lossFn(trainOutput, trainExpectedData)
            totalTrainLoss = loss.item()
            testOutput = net(testInputData)
            loss = lossFn(testOutput, testExpectedData)
            totalTestLoss = loss.item()
        print(f"epoch: {epoch + 1}, trainLoss: {totalTrainLoss:.10f}, testLoss: {totalTestLoss:.10f}")

        if totalTestLoss <= bestError:
            bestError = totalTestLoss
        else:
            errorCounter += 1

        if errorCounter == maxErrors:
            print(f"Zakończono trenowanie sieci z uwagi na osiągnięcie wartości maksymalnej {trainingParams['max_errors']} błędów podczas procesu nauki.")
            print(f"Ostatni wynik spełniający warunek: epoch: {epoch + 1}, trainLoss: {totalTrainLoss:.10f}, testLoss: {totalTestLoss:.10f}")
            break
    return trainOutput.numpy(), testOutput.numpy()
