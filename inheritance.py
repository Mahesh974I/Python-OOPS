
# class Person(object):
      
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age

#     def getName(self):
#         return self.name

#     def getage(self):
#         return self.age
  
#     def isEmployee(self):
#         return False
  
# class Employee(Person):
#     def __init__(self, name, age,salary):
#         super().__init__(name, age)
#         self.salary = salary

   
#     def isEmployee(self):
#         return True

#     def getAge(self):
#         return self.age

#     def getsalary(self):
#         return self.salary



# emp = Person("mahesh",23)  
# print(emp.getName(), emp.isEmployee(), emp.getage())
  
# emp = Employee("raju",23,10000)
# print(emp.getName(), emp.isEmployee(),emp.getsalary())

###
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# class PayrollSystem:
#     def calculate_payroll(self, employees):
#         for employee in employees:
#             print(f'Payroll for: {employee.id} - {employee.name}')
#             print(f'- Check amount: {employee.calculate_payroll()}')
#             print('')

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

a = Employee(123,'mahesh')

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
