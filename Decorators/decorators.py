"""
Decerators are used to change the functionality of the function without modifying the code in it

"""

### Before applying decorators
## importing modules

import math
import time
# class square:
#     def __init__(self):
#         pass
#     def square_root(self,number):
#         self.number = number
#         result = []
#         ## for checking how much time taken to execute
#         start = time.time()
#         result=math.sqrt(self.number)

#         end = time.time()
#         print((end-start)*1000, 'Milliseconds')
#         return result

# class cube:
#     def __init__(self):
#         pass

#     def cubic(self,number):
#         self.number = number
#         start = time.time()
#         result = (self.number**3)
#         end = time.time()
#         print((end-start)*1000, 'Milliseconds')
#         return result



# obj = square()
# print(obj.square_root(40))

# obj1 = cube()
# print(obj1.cubic(3))


"""
The main drawback in this case is to rewrite the code for calculating the executing time.
We can solve this problem by creating a decorator function 
"""
### Creating decorator function for calculating execution time.
def executing_time(func):
    ## creating wrapper function with positional arguments and keyword arguments
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print((end-start)*1000, 'Milliseconds')
        return result
    return inner

class square:
    def __init__(self):
        pass
    ## Declaring decorator class
    @executing_time
    def square_root(self,number):
        self.number = number
        result = []
        result=math.sqrt(self.number)
        return f'square root of {self.number} is {result}'

class cube:
    def __init__(self):
        pass
    @executing_time    
    def cubic(self,number):
        self.number = number
        result = (self.number**3)
        return f'cube of {self.number} is {result}'

obj = square()
print(obj.square_root(100))

obj1 = cube()
print(obj1.cubic(5))