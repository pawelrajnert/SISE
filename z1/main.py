import random

def isMatrixGood(matrix):
    zeroPosition = ""
    uniqueElements = set()
    TAB_SIZE = len(matrix)
    if TAB_SIZE != 16:
        return False
    for i in range (TAB_SIZE):
        uniqueElements.add(matrix[i])
        if matrix[i] == 0:
            zeroPosition = i
    if len(uniqueElements) != TAB_SIZE or zeroPosition == "":
        return False
    return True, zeroPosition

def moveElement(move, matrix, zeroPos):
    if move is "L" and zeroPos % 4 != 0:
        matrix[zeroPos], matrix[zeroPos - 1] = matrix[zeroPos - 1], matrix[zeroPos]
        zeroPos -= 1
    elif move is "R" and zeroPos % 4 != 3:
        matrix[zeroPos], matrix[zeroPos + 1] = matrix[zeroPos + 1], matrix[zeroPos]
        zeroPos += 1
    elif move is "U" and zeroPos >= 4:
        matrix[zeroPos], matrix[zeroPos - 4] = matrix[zeroPos - 4], matrix[zeroPos]
        zeroPos -= 4
    elif move is "D" and zeroPos <= 11:
        matrix[zeroPos], matrix[zeroPos + 4] = matrix[zeroPos + 4], matrix[zeroPos]
        zeroPos += 4
    else: return False
    return True, matrix, zeroPos

def printMatrix(matrix):
    for i in range(0, len(matrix), 4):
        row = matrix[i:i+4]
        print(" ".join(f"{num:4}" for num in row))

testMatrix = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
random.shuffle(testMatrix)
printMatrix(testMatrix)
_, zeroPos = isMatrixGood(testMatrix)
print(zeroPos)
print(moveElement("U", testMatrix, zeroPos))





