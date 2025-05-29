from readData import readData
statData, dynData = readData()
print(statData.shape, dynData.shape)
# Zgadza się dla dynData, dlatego zakładam że dla danych statycznych też się zgadza - nie chce mi się przeliczać 450 plików