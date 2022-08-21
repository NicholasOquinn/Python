#explain program
print('this program displays the projected')
print('increase of tuition with the 3% raise')
#create variables
tuition = 8000
percent = 0.03
total = 8000
#make header
print('YEAR\tINCREASE')
print('--------------')
#create loop statement 
for years in range(1,6):
    new_tuition = tuition * percent
    total += new_tuition
    print(years, '\t', total)
    

