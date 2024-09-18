import re
email = input("Enter your email adress: ")

if re.match(r"^[a-z|A-Z|0-9]+@[a-z|A-Z|0-9]+.[a-z|A-Z]+",email):
    print("Valid")
else:
    print("Invalid")