#prompt user to enter number of each coin
pennies = float(input('enter number of pennies'))
nickles = float(input('enter number of nickles'))
dimes = float(input('enter number of dimes'))
quarters = float(input('enter number of quarters'))

#calculate whether their amount is equal to $1
total = (pennies * 0.01) + (nickles * 0.05) + (dimes * 0.1) + (quarters * 0.25)

if total == 1:
    print('congratulations you won the game!')
elif total < 1:
    print('your amount was less than a dollar')
else:
    print('your amount was more than a dollar')
            
