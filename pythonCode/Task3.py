user_ID = "davidstanchak"
user_PIN = 2837


entry = False
while entry == False:
    check_length_again = True
    while check_length_again == True:

        attempt_PIN = input("Enter your 4-digit pin: \n")
        if len(attempt_PIN) == 4 and attempt_PIN.isdigit():
            correct_PIN = True
        elif len(attempt_PIN) != 4:
            check_length_again = True
            
        else:
            correct_PIN = False
        check_length_again = False

        attempt_ID = input("Enter your user ID which is greater than 10 characters: \n")
    check_length_again == True
    while check_length_again == True:

        if len(attempt_ID) >= 10 and type(attempt_ID) == str:
            correct_ID = True

        else:
            check_length_again = True
        check_length_again = True
            



    if correct_PIN == True and correct_ID == True:
        print("Valid, access permitted")
        entry = True
    else:
        print("Incorrect ID or PIN - Try again")

entry = True