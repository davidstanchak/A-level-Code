myString = input("Please enter a word or phrase to be tested: ").lower()
stack1 = []
for i in range(len(myString)):
    stack1.append(myString[i])

reversedList = []

while len(stack1) != 0:
    reversedList.append(stack1.pop())


if ("".join(reversedList)) == myString:
    print("This is a palindrone")
else: 
    print("This is not a palindrone")