while valid == False:
    user_enter = input("Enter a float")
    for i in range(len(user_enter)):
        letter = user_enter[i]
        if letter == ".":
            print("this is a fload")
        else:
            print()