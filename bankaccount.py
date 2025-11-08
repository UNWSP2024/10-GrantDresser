##
# Program1: Bank Account Class
# Grant Dresser
# 11/7/2025
##

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

    def get_balance(self):
        return self.__balance