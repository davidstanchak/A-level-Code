email = input("Enter your email adress: ")
validAt = False
validDot = False
while validAt == False and validDot == False:
    for i in range(0,len(email)):
        if email[i] == "@":
            validAt = True
        elif email[i] == ".":
            validDot = True

if validAt == True and validDot == True:
    print("Email valid")
else:
    print("Email invalid")