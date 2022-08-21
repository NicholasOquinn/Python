#explain the program
print('this program displays temperatures')
print('0-20 celsius in fahrenheit')

#create header
print('CELSIUS\tFAHRENHEIT')
print('-------------------')

#create loops that calculates temps
for temp in range (21):
    fahrenheit = ((9 / 5) * temp) + 32
    print(temp, '\t', format(fahrenheit, '.1f'))
