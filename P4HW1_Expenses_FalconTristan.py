# CTI-110
# P4HW1-Expenses Calculator
# Tristan Falcon
# 07-6-2021
# 

def main():
    user_account = float (input('Enter amount in account you would like to withdraw from: $'))
    print()
    user_start = user_account
    next_expense = 'y'
    expense_num = 0

    while next_expense == 'y':
        expense = float (input('Enter expense: $',))
        print()
        user_account = user_account - expense
        expense_num += 1
        next_expense = input('Would you like to enter another expense? Enter y for yes or n for no. ')
        print()

    print ('Amount in account before expenses subtracted: $', user_start)
    print ('Number of expenses entered: ', expense_num)
    print ('Amount in account after expenses subtracted: $', user_account)  

main()