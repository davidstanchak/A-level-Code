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
                print("Car succesfully parked.\n")
                
            else:
                print("Parking spot unavailable, Please use a different spot.\n")

    def option3():
        NumberPlate = input("Enter the number plate you would like to clear:\n")
        for i in range(10):
            for j in range(6):
                if CarParkArray[i][j] == NumberPlate:
                    CarParkArray[i][j] = "Empty"


        print("Number plate removed.\n")

    def option4():
        print("Showing car park availability... \n")
        print(CarParkArray)

    UserOptionChoice = str(input("Enter which option you would like to choose (1-5).\nPress 'help' to see all options. \nEnter 0 to end the program. \n"))

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
    elif UserOptionChoice == "help" or UserOptionChoice == "Help":
        print("Option 1 clears all car spaces.\nOption 2 parks a car with your chosen space.\nOption 3 clears a car with specific number plate.\nOption 4 displays parking grid and availability.\n")
        input("Press space to continue to menu again.")
    elif UserOptionChoice == "0":
        print("You have chosen to quit, Goodbye")
        repeat = False