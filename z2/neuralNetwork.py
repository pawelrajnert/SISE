import torch.nn as nn


class NeuralNetwork(nn.Module):

    def __init__(self, hiddenSize, activation):
        if not isinstance(hiddenSize, int) or hiddenSize < 1:
            raise ValueError("Liczba neuronów w warstwie ukrytej musi być dodatnią liczbą całkowitą!")

        super().__init__()
        # ponieważ warstwy wejściowe i wyjściowe składają się z 2 neuronów, wartości te są niemodyfikowalne przez config
        self.inputToHidden = nn.Linear(2, hiddenSize)  # 2 - rozmiar warstwy wejściowej
        self.hiddenToOutput = nn.Linear(hiddenSize, 2)  # 2 - rozmiar warstwy wyjściowej
        if activation == "relu":
            self.activation = nn.ReLU()
        elif activation == "sigmoid":
            self.activation = nn.Sigmoid()
        elif activation == "tanh":
            self.activation = nn.Tanh()
        else:
            raise ValueError("Nieobsługiwana funkcja aktywacji - dozwolone wartości: relu|sigmoid|tanh")

    def forward(self, inputData):       # na razie nie mam pojęcia, po co to xd
        x = self.inputToHidden(inputData)
        x = self.activation(x)
        x = self.hiddenToOutput(x)
        return x
