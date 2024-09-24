import random
GeneratedNumber = random.randint(1,100)
repeat = True
while repeat == True:
    guess = int(input("Guess the number I am thinking of. \n"))
    if GeneratedNumber == guess:
        repeat = False
    elif GeneratedNumber > guess:
        print("No, the number I am thinking of is greater than", guess)
    elif GeneratedNumber < guess:
        print("No, the number I am thinking of is smaller than", guess)

print("You guessed the number correctly! It is", guess)