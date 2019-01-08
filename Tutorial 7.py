# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:46:34 2019

@author: Akib
"""

class BankAccount:
    numOfAccount = 0
    def __init__(self, n,bal):
        self.name = n
        self.balance = bal
        BankAccount.numOfAccount +=1
        
    def displayTotalAccount():
        print( "Total number of account created is",BankAccount.numOfAccount)
    
    def setBalance(self,x):
        self.balance = x
        
    def getBalance(self):
        return self.balance
    
    def withdraw(self,x):
        if self.balance > x:
            self.balance = self.balance - x
        else:
            print("Balance is not sufficient")
            
    
    def deposit(self,y):
        self.balance = self.balance + y
    
    def __str__(self):
        return '%s has %d in the account' %(self.name, self.balance)

a1 = BankAccount("Abu", 100)
b1 = BankAccount("Ali", 200)
BankAccount.displayTotalAccount()
print(a1)
a1.withdraw(200)
a1.withdraw(50)
print(a1.getBalance())
a1.deposit(100)
print(a1.getBalance())
a1.setBalance(50)
print(a1.getBalance())        