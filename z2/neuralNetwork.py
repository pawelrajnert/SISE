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
            output = net(trainInputData)
            loss = lossFn(output, trainExpectedData)
            totalTrainLoss = loss.item()
            output = net(testInputData)
            loss = lossFn(output, testExpectedData)
            totalTestLoss = loss.item()
        print(f"epoch: {epoch + 1}, trainLoss: {totalTrainLoss:.10f}, testLoss: {totalTestLoss:.10f}")
