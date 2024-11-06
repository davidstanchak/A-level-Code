class Dog:

    __name = ""
    __colour = ""

    def __init__(self, myName, myColour):
        self.__name = myName
        self.__colour = myColour

        
    def bark(self, barkTimes):
        for i in range(barkTimes):
            print("Woof!")

        
    def setName(self, newName):
        self.__name = newName

    def getName(self):
        return self.__name


# if myColour == "Unknown":
#             self.colour = input("Enter color of dog")
#         else:
#             self.colour = myColour
doggi = Dog("Phil","Unknown")
print(doggi.getName())