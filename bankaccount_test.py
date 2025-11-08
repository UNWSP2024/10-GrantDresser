##
# Program1.1(test): BankAccount Class Test
# Grant Dresser
# 11/7/2025
##

import bankaccount

def main():
    
    # get starting balance
    start_bal = float(input('Enter your starting balance: '))

    # create a BankAccount object named savings
    savings = bankaccount.BankAccount(start_bal)

    # deposit users paycheck
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    savings.deposit(pay)

    # display balance
    print('Your account balance is $',
          format(savings.get_balance(), ',.2f'), sep='')

    # get amount to withdraw
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)

    # display balance again
    print('Your account balance is $',
          format(savings.get_balance(), ',.2f'), sep='')

# call main
main()