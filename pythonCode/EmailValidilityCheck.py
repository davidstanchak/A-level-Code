import re
email = input("Enter your email adress: ")

if re.match(r"^[a-zA-Z0-9]+@(.*?).[a-zA-Z]+",email):
    print("Valid")
else:
    print("Invalid")