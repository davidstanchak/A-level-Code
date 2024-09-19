CarParkArray = [["empty", "empty", "empty", "empty", "empty", "empty"],
                ["empty", "empty", "empty", "empty", "empty", "empty"],
                ["empty", "empty", "empty", "empty", "empty", "empty"],
                ["empty", "empty", "empty", "empty", "empty", "empty"],
                ["empty", "empty", "empty", "empty", "empty", "empty"],
                ["empty", "empty", "empty", "empty", "empty", "empty"],
                ["empty", "empty", "empty", "empty", "empty", "empty"],
                ["empty", "empty", "empty", "empty", "empty", "empty"],
                ["empty", "empty", "empty", "empty", "empty", "empty"],
                ["empty", "empty", "empty", "empty", "empty", "empty"]]
print(CarParkArray[4][4])

repeat = True
while repeat == True:
    def option1():
        CarParkArray = [["empty", "empty", "empty", "empty", "empty", "empty"],
                        ["empty", "empty", "empty", "empty", "empty", "empty"],
                        ["empty", "empty", "empty", "empty", "empty", "empty"],
                        ["empty", "empty", "empty", "empty", "empty", "empty"],
                        ["empty", "empty", "empty", "empty", "empty", "empty"],
                        ["empty", "empty", "empty", "empty", "empty", "empty"],
                        ["empty", "empty", "empty", "empty", "empty", "empty"],
                        ["empty", "empty", "empty", "empty", "empty", "empty"],
                        ["empty", "empty", "empty", "empty", "empty", "empty"],
                        ["empty", "empty", "empty", "empty", "empty", "empty"]]
        print("All car park spaces are now empty. \n")
    def option2(placeAvailable):
        while placeAvailable == False:
            NumberPlate = input("Enter the number plate in form [#### ###] (UK STANDARD): \n")
            print("There are 10 rows and 6 columns in this carpark - so, there are 60 spaces in this parking lot. \n")
            row = int(input("Which row would you like to park in: \n"))
            column = int(input("And, which column would you like to park in: \n"))
            if CarParkArray[row-1][column-1] == "empty":
                CarParkArray[row-1][column-1] = NumberPlate
                placeAvailable = True
                
            else:
                print("Parking spot unavailable, Please use a different spot")

    def option3():
        NumberPlate = input("Enter the number plate you would like to clear")
        CarParkArray = CarParkArray.replace(NumberPlate, "empty")
        print("Number plate removed")

    def option4():
        print("Showing car park availability... \n")
        print(CarParkArray)

    UserOptionChoice = input("Enter which option you would like to choose (1-5).\n Press 'help' to see all options. \n Enter 0 to end the program. \n")

    if UserOptionChoice == "1":
        print("You have chosen option: ", UserOptionChoice)
        option1()
    elif UserOptionChoice == "2":
        print("You have chosen option: ", UserOptionChoice)
        placeAvailable = False
        option2(placeAvailable)
    elif UserOptionChoice == "3":
        print("You have chosen option: ", UserOptionChoice)
        option3()
    elif UserOptionChoice == "4":
        print("You have chosen option: ", UserOptionChoice)
        option4()
    elif UserOptionChoice == "0":
        print("You have chosen to quit, Goodbye")
        Repeat = False