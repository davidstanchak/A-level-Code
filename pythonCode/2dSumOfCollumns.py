array = [["1","2","3","4","5"],
         ["6","7","8","9","10","11","12"],
         ["13","14","15","16","17","18", "19","20"]]
#          20,  23, 26,  29,  32,  29, 31, 20

def zeroPlacer(array):
    global greatestArrayLength
    greatestArrayLength = 0
    for i in range(len(array)):
        lengthOfRow = len(array[i])
        if lengthOfRow > greatestArrayLength:
            greatestArrayLength = lengthOfRow
    
    for i in range(len(array)):
        while len(array[i]) != greatestArrayLength:
            array[i].append(0)
            
    return array
    
array = zeroPlacer(array)

def sum():
    sumArray = []
    for i in range(greatestArrayLength):
        sumOfCurrentCollumn = 0
        for j in range(len(array)):
            sumOfCurrentCollumn += int(array[j][i])
        
        sumArray.append(sumOfCurrentCollumn)
    return sumArray
            
sumArray = sum()
print(f"here are the sums of the collumns: {sumArray}")#