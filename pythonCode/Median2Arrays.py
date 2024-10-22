arrayOne = [50,24,8]
arrayTwo = [24,0,5]

for i in range(len(arrayOne+arrayTwo)):
    if (len(arrayOne) != i):
        if (arrayOne[i] > arrayOne[i+1]):
            arrayOne[i+1] = arrayOne[i]

    if arrayTwo[i] > arrayTwo[i+1] and (arrayTwo[i] > arrayTwo[i+1]):
        arrayTwo[i+1] = arrayOne[i]

for i in range(len(arrayOne)):
    if i != 
        if arrayOne[i] > arrayOne[i+1]:



print(arrayOne,arrayTwo)

