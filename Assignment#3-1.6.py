from math import pi
from msilib.schema import SelfReg

class Account:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def getID(self):
        return self.id

    def getName(self):
        return self.name
    
    def getBalance(self):
        return self.balance

    def Credit(self, balance):
        Amount = Amount + balance
        return Amount 

    def Debit(self, balance, amount):
        if amount <= balance:
            balance = amount - balance
            print('Balance = ' ,balance) 
        else: 
            print('Amount Exceeded Balance')
        return balance
    
    # def TransferTo(self, amount, AnotherAcc):
    
    
NewAccount = Account(10, 'Hisham Refaee', 2500)
print('ID = ',NewAccount.getID())
print('Name = ',NewAccount.getName())
print('Balance = ',NewAccount.getBalance())
print('Credit = ',NewAccount.Credit())
print('Debit = ',NewAccount.Debit())