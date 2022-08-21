start_num = int(input('Starting number of organisms: '))
avg = float(input('Average daily increase: '))
Days = int(input('Number of days to multiply: '))
pop = start_num
print('Day Approximate\tPopulation')
print('---------------------------')

for number in range(1, Days + 1):
    pop = pop + (pop * avg)
    print(number, '\t', format(pop, '.2f'))
    
    
