import re
email = input("Enter your email adress: ")

if re.match(r"^(.*?)@(.*?).(.*?)",email):
    print("Valid")
