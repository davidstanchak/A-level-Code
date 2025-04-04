array = [["1","2","3","4","5"],
         ["6","7","8","9","10","11","12"],
         ["13","14","15","16","17","18", "19","20"]]

FinalArray = [[1,6,13],[2,7,14],[3,8,15],[4,9,16],[5,10,17],[11,18],[12,19],[20]]



def noneAdd(array):
    global greatestArrayLength
    greatestArrayLength = 0
    for i in range(len(array)):
        lengthOfRow = len(array[i])
        if lengthOfRow > greatestArrayLength:
            greatestArrayLength = lengthOfRow
    
    for i in range(len(array)):
        while len(array[i]) != greatestArrayLength:
            array[i].append("0")
            
    return array

def transpose(array):
    collumnToRow = []
    transposedArray = []
    for i in range(greatestArrayLength):
        for j in range(len(array)):
            collumnToRow.append(array[j][i])

        transposedArray.append(collumnToRow)
    return transposedArray

def zeroRemove(transposedArray):
    removeZeroRow = []
    transposedArrayFinal = []
    for i in range(len(transposedArray)):
        for j in range(greatestArrayLength):
            if transposedArray[i][j] != 0:
                removeZeroRow.append(array[j][i])

        transposedArrayFinal.append(removeZeroRow)
    return transposedArrayFinal
    

array = noneAdd(array)
t1 = transpose(array)
print(t1)