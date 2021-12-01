class car:

    def __init__(self, name, mileage):
        self._name = name                #protected variable
        self.mileage = mileage 

    def description(self):                
        return f"The {self._name} car gives the mileage of {self.mileage}km/l"


obj = car("BMW 7-series",39.53)

#accessing protected variable via class method 
print(obj.description())

#accessing protected variable directly from outside
print(obj._name)
print(obj.mileage)


class car1:

    def __init__(self, name, mileage):
        self.__name = name                #private variable
        self.mileage = mileage 

    def description1(self):                
        return f"The {self.__name} car gives the mileage of {self.mileage}km/l"


obj1 = car1("BMW 5-series",20)

#accessing private variable via class method 
print(obj1.description1())

#accessing private variable directly from outside
# print(obj1.__name)## if i run it will throws error bcz it is a private variable

print(obj1.mileage)
print(obj1._car1__name)


###  ABSTRACTION


from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self,name):
        self.name = name

    def description(self):
        return ("This the description function of class car.")

    @abstractmethod
    def price(self,x):
        pass
class new(Car):
    def price(self,x):
        return (f"The {self.name}'s price is {x} lakhs.")

obj = new("Honda City")

print(obj.description())
print(obj.price(25))