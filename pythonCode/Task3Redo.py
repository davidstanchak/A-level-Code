import random
id_attempts = 0

password = "helloworld"
pin = 4545
userID = "mynameisdavidhello"
def login(userID,pin,password):
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        userID_enter = input("Enter you 10-character user ID: \n") 
        attempts += 1
        if userID_enter == userID:
            attempts = 0
            max_attempts = 1
            while attempts < max_attempts:
                pin_enter = input("Please enter your pin: ")
                if pin_enter == pin:
                    attempts = 0
                    max_attempts = 3
                    while attempts < max_attempts:
                        print("TEMP") # TODO: implement functionallity
                else:
                    print("Access denied.")
        elif attempts == max_attempts:
            print("Access denied")
            return
        else:
            print(f"User ID incorrect {max_attempts - attempts} attempts left")

        # PIN_attemps = 0
        # userPIN_enter = input("Enter your 4-digit PIN: \n")
        # PIN_attemps += 1
        # if userPIN_enter == pin:
        #     second = True
        #     PIN_attemps = 3
        # random_attemps = 0
        # while random_attemps < 3:
        #     guess_one = False
        #     guess_two = False
        #     guess_three = False
        #     while guess_one != True and guess_two != True and guess_three != True:
        #         first_random = random.randint(1, len(password))
        #         first_guess = input("enter character place", str(first_random) ," of your password. \n")
        #         if first_guess == password[first_random]:
        #             guess_one = True
                
        #         second_random = first_random
        #         while second_random == first_random:
        #             second_random = random.randint(len(password))
        #         second_guess = input("enter character place", second_random," of your password.")
                
        #         if second_guess == password[second_random]:
        #             guess_two = True
        #         third_random = random.randint(len(password))

        #         third_guess = str(input("enter character place", third_random," of your password."))
        #         third_random = random.randint(len(password))
        #         third_random = second_random
        #         while third_random == second_random:
        #             third_random = random.randint(len(password))
        #         if second_guess == password[second_random]:
        #             guess_three = True
        #         random_attemps = 4
        #         if guess_one == True and guess_two == True and guess_three == True:
        #             third = True

            
        #     third = True
    
    # if first == True and second == True and third == True:
    #     print("access granted ")
    # else:
    #     print("access denied")

login(userID,pin,password)