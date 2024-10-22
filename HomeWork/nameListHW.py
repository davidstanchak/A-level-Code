def add_name(array):
    name = input("Enter the name that you would like to add: \n")
    pos = int(input("Enter the pos that you would like to place it in (1-10): \n"))
    if pos in range(1,10):
        if array[pos-1] != "random":
            print("Replacing ",array[pos-1]," located at position ",pos," with ",name)
        else:
            print("Empty position, inserting",name,"into position",pos)
        array[pos-1] = name
    else:
        print("Position",pos,"is invalid, sending you to Menu...\n")

def display_list(array):
    final = []
    for i in range(len(array)):
        if array[i] != "random":
            final.append(array[i])
    print(final)
    
def displayMenu():
    redo = True
    array = ["random"]*10
    while redo == True:
        choice = input("Choose an option. Add name (1), Display list (2), Quit (3). \n")
        if choice == "1" or choice == "2" or choice == "3":
            if choice == "3":
                print("Program terminating")
                redo = False
            elif choice == "2":
                display_list(array)
            elif choice == "1":
                add_name(array)
        else:
            print("invalid input. Enter either 1,2 or 3.")

displayMenu()