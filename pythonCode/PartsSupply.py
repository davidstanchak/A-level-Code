redo = True
TotalParts = 0
while redo == True:
    partNumber = str(input("Enter a part number: "))
    if len(partNumber) != 4:
        print("Invalid part number, part number must be 4 digits.")
        redo = True
    elif partNumber == "9999":
        redo == False
    else:
        TotalParts = TotalParts + 1

        runNum = partNumber[3]
        print(runNum)

        if runNum == "6" or runNum == "7" or runNum == "8":
            print("This part is an old model.")
        else:
            print("This part is a new model.")
        redo == False