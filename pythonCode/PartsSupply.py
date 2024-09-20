redo = True #variable to terminate code when user wishes
TotalParts = 0 ##count for new parts
OldParts = 0 #count for old parts
while redo == True:
    partNumber = str(input("Enter a part number: "))
    if len(partNumber) != 4:   #asks user to re-enter part number as it is invalid
        print("Invalid part number, part number must be 4 digits.")
        redo = True
    elif partNumber == "9999":  #used to stop the code and output results
        redo = False  
    else:
        TotalParts = TotalParts + 1

        runNum = partNumber[3] #assigning last/4th digit of number to runNum so it can be checked.
        if runNum == "6" or runNum == "7" or runNum == "8":  # 6,7,8 indicates the part is old
            OldParts = OldParts + 1   #OldParts is incremented by 1.

print(OldParts, " Out of ", TotalParts," valid parts entered, are old") 
#finally user is told how many old parts there are out of the ones they entererd.