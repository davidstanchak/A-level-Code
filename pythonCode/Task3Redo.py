import random
id_attempts = 0

password = "helloworld"
pin = "4545"
userID = "mynameisdavidhello"
def login(userID, pin, password):
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        userID_input = input("Enter you 10 character user id: ")
        if userID_input == userID:
            print("Correct user id")
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Incorrect user id. You only have {max_attempts - attempts} attempts left.")
            else:
                print("Incorrect user id. Access denied.")
                return
            
    pin_input = input("Enter your pin: ")
    if pin_input != pin:
        print(f"{pin_input} {pin}")
        print("Access denied. No more attempts left.")
        return
        
    attempts = 0
    while attempts < max_attempts:
        positions = random.sample(range(1, len(password) + 1), 3)
        correct = True
        for pos in positions:
            password_char_input = input(f"Enter character {pos} of your password: ")
            if password_char_input != password[pos-1]:
                correct = False
                break
        if correct:
            print("Access granted.")
            return
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Incorrect password. You only have {max_attempts - attempts} attempts left")
            else:
                print("Incorrect password.")
                return

login(userID, pin, password)