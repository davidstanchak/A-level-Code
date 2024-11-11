#Task 1: Extract Part of an Email Address
email = "19stanchakD@centralfoundationboys.co.uk"
domain = []
start = False
for i in range(len(email)):
    if start:
        if email[i] == ".":
            domain = "".join(domain)
            break
        domain.append(email[i])
    elif email[i] == "@":
        start = True
print(domain)

#Task 2: Name Abbreviation
fullName = "First Middle Last"
initials = [fullName[0]]
for j in range(len(fullName)):
    if fullName[j] == " ":
        initials.append(fullName[j+1])
print("".join(initials))

#Task 3: Validate Date Format
date = "11/11/2024"
sections = date.split("/")

if len(sections) == 3:
    day, month, year = sections
    if len(day) == 2 and len(month) == 2 and len(year) == 4:
        if day.isdigit() and month.isdigit() and year.isdigit():
            print("Valid Date")
        else:
            print("Invalid Date")
    else:
        print("Invalid Date")
else:
    print("Invalid Date")

#Task 4: Extract Substring Between Symbols
phrase = "Find [this] substring"
substring = []
start = False

for i in range(len(phrase)):
    if start:
        if phrase[i] == "]":
            substring = "".join(substring)
            break
        substring.append(phrase[i])
    elif phrase[i] == "[":
        start = True
print(substring)

#Task 5: String Repetition Checker
original = "xyzxyzxyz"

for i in range(1, len(original) // 2 + 1):
    substring = original[:i] 
    if substring * (len(original) // len(substring)) == original:
        print(f"{substring} is the shortest possible string that can form the original string when repeated.")
        break
else:
    print("No repeating substring found")