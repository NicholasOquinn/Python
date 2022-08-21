print('this program displays how much the ocean ' +
      'has risen over 25 years')
print('YEAR\tAMOUNT RISEN')
print('------------------')

for years in range(1, 26, 1):
    risen = 1.6 * years
    print(years, '\t', format(risen, '.1f'))
    
