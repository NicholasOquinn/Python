days = int(input('Enter number of days: '))
total = 0
print('Day\tAMOUNT')
print('-----------')
for pennies in range(1, days+1, 1):
    pennies *= 2
    print(days, '\t', '$', format(pennies, '.1f'))
