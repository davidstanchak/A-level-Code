class Stack():
    #constructor
    def __init__(self, firstData):
        self.top = Node(firstData)

    def pop(self):
        if self.top is None:
            return "Stack Underflow: Stack Empty"
        
        # find the top, return top, change the top so it points to the tops previous
        current = self.top 
        self.top = current.prev # changing top to previous item, essentialy -1 in arrays
        return current.data # return data of the popped item
    
    def push(self, letter):
        newNode = Node(letter)
        newNode.prev = self.top
        self.top = newNode

    def peek(self):
        print(self.top.data)

class Node():
    #constructor
    def __init__(self, theData): 
        self.data = theData
        self.prev = None
#################################################################################
enterWord = str(input("Enter a word: ")).lower()
word = Stack(enterWord)

l = len(enterWord)
palindrome = True

for i in range(l):
    word.push(enterWord[i])

j=0
while j< l and palindrome == True:
    if enterWord[j] != word.pop():
        palindrome = False
    j += 1

if palindrome == True:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")