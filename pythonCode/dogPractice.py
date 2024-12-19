'''
Create a Class for a dog in python. '
Implement private attributes using the _attribute approach in python. 
When a dog is instantiated the constructor takes in two parameters, the name and colour. 
These are the only attributes within the dog class. 
Also create a method that will take in a parameter integer and then output "Woof!" the number of times the value of the parameter. 
Create the necessary getter and setter methods for the object.
'''

class Dog:

    # private attributes
    ___name = ""
    ___colour = ""

    # constructor
    def __init__(self,myName,myColour):
        self.___name = myName 
        self.___colour = myColour 
        
    # method to action a bark
    def bark(self,barkTimes):
        for i in range(barkTimes):
            print("Woof!")

    #getter
    def getName(self):
        return  self.___name
    #setter
    def setName(self, newName):
        self.___name  = newName



##### main program ###

myDog = Dog("Fido", "Brown")
myDog2 = Dog
barkTimes = int(input("Enter a number: "))
print(myDog)
myDog.bark(barkTimes)