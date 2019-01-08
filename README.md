# Basic-Python-code
Create a BankAccount class, which has below methods
a. Constructor that receives the account holder name and the initial balance in the account.
b. A static method displayTotalAccount that displays the total number of accounts that
have been created.
c. A setBalance method that sets the account with a new balance.
d. A getBalance method that returns the current account balance.
e. A withdraw method that withdraws certain amount from the account.
f. A deposit method that deposits certain amount into the account.
g. A __str__ method to display the account holder name and current balance.



Example of how above methods are used is illustrated below:
a1 = BankAccount("Abu", 100)
b1 = BankAccount("Ali", 200)
BankAccount.displayTotalAccount()
# "Total number of account created is 2" will be displayed.
print(a1)
# "Abu has 100 in the account" will be displayed.
a1.withdraw(200)
# "Balance is sufficient" will be displayed.
a1.withdraw(50)
print(a1.getBalance())
# "50" will be displayed.
a1.deposit(100)
print(a1.getBalance())
# "150" will be displayed.
a1.setBalance(50)
print(a1.getBalance())
# "50" will be displayed.
