class Vehicle:
    
    __make = None
    __model = None
    __year = None
    
    def __init__(self, theMake, theModel, theYear):
        self.__make = theMake
        self.__model = theModel
        self.__year = theYear
    
    def car(self, convertible, doors, tinted):
        self.__convertible = convertible
        self.__doors = doors
    
    def getAll(self):
        theMake, theModel, theYear = self.__make, self.__model, self.__year
        return theMake, theModel, theYear
         
        
    def truck(self, load, wheels):
        self.__load = load
        self.__wheels = wheels
        
        loadSpread = load/wheels
        return loadSpread
        
    def motorcycle(self, passengerCap):
        self.__passengerCap = passengerCap
        
car1 = Vehicle("Ford", "Mustang", "2015") #initiation with make, model, year as attributes
print(car1.car(True, "4", True)) #specifying car1 as a car to add more attributes to it. 
print(car1) #prints location in memory.

truck1 = Vehicle("Mercedes", "Sprinter", "2020")
loadSpread = truck1.truck(8000, 18) #prints loadSpread
print(loadSpread)

motorcycle1 = Vehicle("BMW", "F900R", "2012")
motorcycle1.motorcycle(4)

print(car1.getAll()) #prints init

