budget = int(input('Enter monthly budget: '))
total = 0.0
keep_going = 'Y'
while keep_going == 'y' or keep_going == 'Y':
    expenses = int(input('Enter Amount Spent: '))
    total += expenses
    keep_going = input('enter Y to continue or N to stop')

    if keep_going == 'N':
        print(total)
        if total > budget:
            print('You have gone over your budget')
        if total < budget:
            print('you are under your budget')
