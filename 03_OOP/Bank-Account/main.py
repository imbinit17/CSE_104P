# Class Definition: Define a class named BankAccount.

# Attributes: Include the following attributes in the constructor (__init__ method):

#     account_number: (String) A unique identifier for the account.
#     account_holder: (String) Name of the account holder.
#     balance: (Float) Initialize with a default value of 0.0 to represent the account balance.

# Methods: Add the following methods to the class:

#     - deposit(amount): Accepts an amount and adds it to the balance.
#     - withdraw(amount): Accepts an amount and subtracts it from the balance if sufficient funds are available.
#     - check_balance(): Prints the current balance.
#     - display_details(): Prints the account holder's details and current balance.

class BankAccount:
    def __init__(self,ac_no:str,name:str):
        self.account_number = ac_no
        self.account_holder = name
        self.bal = 0.0
        
    def deposit(self,amt:int):
        if(amt>0):
            self.bal += amt
            print(f'Rs {amt} deposited successfully into A/c No : {self.account_number}')
            self.check_balance()
        elif amt-amt%1>0 or amt<=0:
            print('Deposit failed as amount should be non decimal positive number')

    def withdraw(self,amt:int):
        if amt>0 and self.bal>=amt:
            self.bal-=amt
            print(f'Rs {amt} withdrawn successfully.')
            self.check_balance()
        elif amt>=self.bal:
            print("Withdraw failed ! Insufficient funds.")
        elif amt-amt%1>0 or amt<=0:
            print('Withdraw failed as amount should be non decimal positive number')
            
    def check_balance(self):
        print(f'Balance : {self.bal}')
        
    def display_details(self):
        print(f'Account Holder Name : {self.account_holder}')
        print(f'Account Number : {self.account_number}')
        self.check_balance()
        
            