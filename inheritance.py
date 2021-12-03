"""
Inheritance is nothing but the acquiring the properities of the parent classes.
Below is the example for implementing inheritance
"""

## creating parent class person
class Person(object):
      
    def __init__(self, name,age):
        self.name = name
        self.age = age
    ## creating methods for the parent class
    def getName(self):
        return self.name

    def getage(self):
        return self.age
  
    def isEmployee(self):
        return False

## Creating child class Employee which acquires the properties of person class
class Employee(Person):
    def __init__(self, name, age,salary):
        ## using super keyword initialising the init variables of parent class
        super().__init__(name, age)
        self.salary = salary

   
    def isEmployee(self):
        return True


    def getsalary(self):
        return self.salary




  
emp = Employee("raju",25,1000000)
print('employee name is ',emp.getName(), 'and his age is ',emp.getage(),'salary is',emp.getsalary())

### Another Example for inheritance

class Car:
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price

    def description(self,speed):
        self.speed = speed
        return f'Our {self.name} {self.model} will go max at a apeed of {self.speed}'

class Name(Car):
    def __init__(self, name, model, price,mailage,horsepower):
        super().__init__(name, model, price)
        self.milage = mailage
        self.horsepower = horsepower
    def carmilage(self):
        return self.milage
    def hp(self):
        return self.horsepower
# a = Car('BMW','i20',2000000)
b = Name('BMW','i20',2000000,15,720)
print(b.description(399),'with horsepower of',b.hp(),'and with milage of',b.carmilage())



  
