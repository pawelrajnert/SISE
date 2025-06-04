from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler
import torch


def scaleData(statData, dynData, scalerToUse):
    if scalerToUse == "standard":
        scaler = StandardScaler()
    elif scalerToUse == "minmax":
        scaler = MinMaxScaler()
    elif scalerToUse == "maxabs":
        scaler = MaxAbsScaler()
    else:
        raise ValueError("Zastosowano nieobsługiwany typ skalowania danych")
    print(scaler)
    scaler.fit(statData)  # skalujemy na podstawie danych treningowych
    statScaled = scaler.transform(statData)
    dynScaled = scaler.transform(dynData)  # tę samą skalę stosujemy też dla danych testowych
    return statScaled, dynScaled, scaler


def reverseScale(scaledData, scaler):  # funkcja zachowywałaby się tak samo dla danych statycznych i dynamicznych
    return scaler.inverse_transform(scaledData)  # zatem wystarczy uogólniona wersja dla obu danych


def numpyToTorch(data, columns):  # przekształcenie danych do postaci, którą można wprowadzić do sieci
    if columns in ("01", "10"):
        return torch.tensor(data[:, :2], dtype=torch.float32)
    elif columns in ("23", "32"):
        return torch.tensor(data[:, 2:], dtype=torch.float32)
    else:
        raise ValueError("BŁĄD - niepoprawne kolumny")
