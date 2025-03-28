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
    
    def push(self, newData):
        newNode = Node(newData)
        newNode.prev = self.top
        self.top = newNode

    def peek(self):
        print(self.top.data)

class Palindrome:
    def __init__(self):
        self.pal = []
    
    def palindrome(self):
        for i in range(self.top+1):
            self.pal.append(people.pop())
        

        

        

    
    


class Node():
    #constructor
    def __init__(self, theData): 
        self.data = theData
        self.prev = None

people = Stack("Altaf")

people.push("Bob")
people.peek("John")




