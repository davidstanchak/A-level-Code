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
UserOptionChoice = input("Enter which option you would like to choose (1-5) or press 'help' to see all options.")

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
def option2():
    NumberPlate = input("Enter Number plate in form [#### ###]")
    

if UserOptionChoice == "1":
    print("You have chosen option: ", UserOptionChoice)
    option1()
elif UserOptionChoice == "2":
    print("You have chosen option: ", UserOptionChoice)
    option2()

