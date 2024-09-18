import re
passwordValid = True
while passwordValid != False:
    password = str(input("Create a password: "))
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\w)",password) and len(password) < 8:
        print("Password Valid")
    else:
        print("Password Invalid")
        passwordValid = False
        