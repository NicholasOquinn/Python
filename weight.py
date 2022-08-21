print('this program calculates your projected weight')
print('for the next 6 months if you follow the diet')
weight = float(input('Enter your weight: '))
print('MONTH\tWEIGHT')
print('-------------')

for months in range(1, 7):
    weight -= 4
    print(months, '\t', weight)
    



