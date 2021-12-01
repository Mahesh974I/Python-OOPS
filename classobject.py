class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def breed(self,bname):
        self.bname = bname
        return f'{self.name} belongs to {self.bname}'

d = Dog('Tommy',9)
print(d.description())
b = d.breed('lab')
print(b)


### Example

class Cab:
    
    #Initialise variables for first iteration
    numberofcabs  = 0
    numpassengers = 0

    def __init__(self,driver,kms,places,pay,passengers):
        self.driver = driver
        self.running = kms
        self.places = places
        self.bill = pay
        Cab.numberofcabs  =  Cab.numberofcabs + 1
        Cab.numpassengers =  Cab.numpassengers + passengers

    #Returns price of cab fare per km
    def rateperkm(self):
        return self.bill/self.running
        
    #Returns number of cabs running         

    def noofcabs(cls):
        return cls.numberofcabs

    #Returns average number of passengers travelling in a cab

    def avgnoofpassengers(cls):
        return int(cls.numpassengers/cls.numberofcabs)

firstcab  = Cab("Ramesh", 80, ['Delhi', 'Noida'], 2200, 3)
secondcab = Cab("Suresh", 60, ['Gurgaon', 'Noida'], 1500, 1)
thirdcab  = Cab("Dave", 20, ['Gurgaon', 'Noida'], 680, 2)

print(firstcab.rateperkm())