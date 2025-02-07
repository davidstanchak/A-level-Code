array = [["1","2","3","4","5"],
         ["6","7","8","9","10","11","12"],
         ["13","14","15","16","17","18", "19","20"]]

def noneAdd(array):
    global greatestArrayLength
    greatestArrayLength = 0
    for i in range(len(array)):
        lengthOfRow = len(array[i])
        if lengthOfRow > greatestArrayLength:
            greatestArrayLength = lengthOfRow
    
    for i in range(len(array)):
        while len(array[i]) != greatestArrayLength:
            array[i].append(None)
            
    return array

def transpose():
    collumnToRow = []
    transposedArray = []
    for i in range(greatestArrayLength):
        for j in range(len(array)):
            collumnToRow += str(array[j][i])

        transposedArray.append(collumnToRow)
    return transposedArray

t1 = transpose()
print(t1)



