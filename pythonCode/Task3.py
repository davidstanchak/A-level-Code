user_ID = davidstanchak
user_PIN = 2837


entry = False
while entry == False:
    attempt_PIN = input("Enter your 4-digit pin")
    if len(attempt_PIN) == 4 and attempt_PIN.isdigit():
        print(attempt_PIN, " is valid")
        correct_PIN = True
    else:
        correct_PIN = False
    attempt_ID = input("Enter your 10-character user ID")
    
    if len(attempt_ID) >= 10 and type(attempt_ID) == str:
        compare_ID = True

        print(attempt_PIN, " is valid")
        correct_ID = True

        if correct_PIN == True and correct_ID == True:
            print("Valid, access permitted")
            entry = True
        

        else:
            print("Incorrect ID or PIN - Try again")
            






