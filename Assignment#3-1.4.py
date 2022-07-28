from math import pi
from msilib.schema import SelfReg

class Employee:
    def __init__(self, id, firstName, lastName, salary):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def getID(self):
        return self.id

    def getfirstName(self):
        return self.firstName

    def getlastName(self):
        return self.lastName
    
    def getName(self):
        return self.firstName, self.lastName
    
    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary   

    def getAnnualSalary(self):
        Annual = self.salary * 12
        return Annual

    def RaiseSalary(self):
        Raise = (self.salary * 0.1) + self.salary
        return Raise
    
NewEmp = Employee(10, 'Hisham', 'Refaee', 2500)
print('ID = ',NewEmp.getID())
print('Name = ',NewEmp.getName())
print('Salary = ',NewEmp.getSalary())
print('Annual Salary = ',NewEmp.getAnnualSalary())
print('Raise Salary = ',NewEmp.RaiseSalary())