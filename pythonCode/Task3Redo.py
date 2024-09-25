import random
ID_attemps = 0

password = "helloworld"
pin = 4545
userID = "mynameisdavidhello"

while ID_attemps < 3:
    userID_enter = input("Enter you 10-character user ID: \n")
    ID_attemps += 1
    if userID_enter == userID:
        first = True
        ID_attemps = 4
PIN_attemps = 0
while PIN_attemps < 1:
    userPIN_enter = input("Enter your 4-digit PIN: \n")
    PIN_attemps += 1
    if userPIN_enter == pin:
        second = True
        PIN_attemps = 3
random_attemps = 0
while random_attemps < 3:
    guess_one = False
    guess_two = False
    guess_three = False
    while guess_one != True and guess_two != True and guess_three != True:
        first_random = random.randint(1, len(password))
        first_guess = input("enter character place", str(first_random) ," of your password. \n")
        if first_guess == password[first_random]:
            guess_one = True
        
        second_random = first_random
        while second_random == first_random:
            second_random = random.randint(len(password))
        second_guess = input("enter character place", second_random," of your password.")
        
        if second_guess == password[second_random]:
            guess_two = True
        third_random = random.randint(len(password))

        third_guess = str(input("enter character place", third_random," of your password."))
        third_random = random.randint(len(password))
        third_random = second_random
        while third_random == second_random:
            third_random = random.randint(len(password))
        if second_guess == password[second_random]:
            guess_three = True
        random_attemps = 4
        if guess_one == True and guess_two == True and guess_three == True:
            third = True

    
    third = True
   
if first == True and second == True and third == True:
    print("access granted ")
else:
    print("access denied")