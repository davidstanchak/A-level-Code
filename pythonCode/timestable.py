def multiples(table,startnum,endnum,pupilName):
    array = [startnum]
    for i in range(startnum,endnum):
        if i != endnum-startnum:
			array[i+1] = startnum
            print(str(table)," X ", str(array[i]), " = ", (array[i]*table))
		    
pupilName = input("Enter your name")
table = int(input("Enter the table"))
startnum = int(input("Enter the start number"))
endnum = int(input("Enter the end number"))
multiples(table,startnum,endnum,pupilName)

def multiples(table,startnum,endnum,pupilName):
    