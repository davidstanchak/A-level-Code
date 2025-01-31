array = [["1","2","3","4","5"],["6","7","8","9","10"],["11","12","13","14","15"]]

sumList = [None, None, None]
def Sum(array, sumList):
    for i in range(len(array)):
        sum = 0
        for j in range(len(array[i])):
            sum += int(array[i][j])
            
        sumList[i] = sum
    return sumList
            

sumListPrint = Sum(array, sumList)
print(sumListPrint)