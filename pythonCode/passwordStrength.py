import re
passwordValid = False
while passwordValid == False:
    password = str(input("Create a password: "))
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\w)",password) and len(password) >= 8:
        print("Password Valid")
        passwordValid = True
    else:
        print("Password Invalid")
        passwordValid = False
        