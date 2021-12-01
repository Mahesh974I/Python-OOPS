
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
    


    def __init__(self,driver,kms,places,pay,passengers):
        self.driver = driver
        self.running = kms
        self.places = places
        self.bill = pay
        self.passengers = passengers


    #Returns price of cab fare per km
    def rateperkm(self):
        return self.bill/self.running
        
       



firstcab  = Cab("Ramesh", 80, ['Delhi', 'Noida'], 2200, 4)
secondcab = Cab("Suresh", 60, ['Gurgaon', 'Noida'], 1500, 1)
thirdcab  = Cab("Dave", 20, ['Gurgaon', 'Noida'], 680, 2)
print(firstcab.driver)
print(secondcab.passengers)
print(thirdcab.places)
print(firstcab.rateperkm())
print(secondcab.rateperkm())
print(thirdcab.rateperkm())


### 

class Check:
    
    def __init__(self,number):
        self.number = number

    def primenumber(self):
        if self.number == 0 and self.number == 1:
            return 'Not a prime number'
        else:
            for i in range(2, int(self.number**(1/2)) +1 ):
                if self.number%i == 0:
                    return 'Not a Prime Number'
            return 'prime Number'
    def evennumber(self):
        if self.number % 2 == 0:
            return 'Even Number'
        else:
            return 'ODD number'

    def pallindrome(self):

        temp = self.number
        result = 0

        # run the loop untill temp is not equal to zero
        while(temp != 0) :
            
            remainder = temp % 10

            result =  result * 10 + remainder

            # integer division
            temp //= 10

        # check result equal to the num attribute or not
        if self.number == result :
            return (self.number,"is Palindrome")
        else :
            return (self.number,"is not Palindrome")

## Testing

if __name__ == '__main__':
    num = 11
    
    # make an object of Check class
    check_prime = Check(num)
    
    # method calling
    print(check_prime.primenumber())
    
    num = 14
    check_prime = Check(num)
    print(check_prime.primenumber()) 
    num = 6
    even = Check(num)
    print(even.evennumber())
    num = 121
    pallindrome = Check(num)
    print(pallindrome.pallindrome())
    num = 586
    pallindrome = Check(num)
    print(pallindrome.pallindrome())
