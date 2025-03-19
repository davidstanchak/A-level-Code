myString = input("Please enter a word or phrase to be tested: ").lower() #converts input to lowercase to ignore whether letter is capital or not.
stack1 = [] 
for i in range(len(myString)):
    stack1.append(myString[i]) #turning input into a stack

reversedList = []

while len(stack1) != 0:
    reversedList.append(stack1.pop())  #popping the stack and appending it to a new stack called reversedList, essentially reversing stack

if ("".join(reversedList)) == myString: #checking if the reversedList (joined up together) is equal to the original input to see if it is a palindrome.
    print("This is a palindrome")
else: 
    print("This is not a palindrome") 