quit = False
dogs = []
while quit != True:
    def find(name):
        for i in range(len(dogs)):
            if dogs[i][1] == name:
                print(f"We have {name} in our inventory")
            else:
                print(f"We cannot find {name} in our inventory.")
        print("You have found a dog")
    def sell(name):
        for i in range(len(dogs)):
            if dogs[i][1] == name:
                print(f"We have removed {name} from our inventory")
            else:
                print("We have been unable to remove {name} from our inventory because we cannot find him/her in our system.")
    def add(new, name):
        dogs.append(new)
        print(f"You have added {name}")

    choice = int(input("Do you want to find(1), sell(2), or add(3) dogs. Type anything else to quit."))
    if choice == 1:
        name = input("What dog would you like to find?")
        find(name)
    elif choice == 2:
        name = input("What dog would you like to sell?")
        sell(name)
    elif choice == 3:
        name = input("What is the dogs name")
        colour = input("What is the dogs colour")
        breed = input("What is the dogs breed")
        add([name, colour, breed], name)
    else:
        print("You have quit")
        quit = True