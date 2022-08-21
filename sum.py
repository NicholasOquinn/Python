#define total
total = 0.0
#create loop that asks for positive numbers
#and adds them up until a negative is entered
#then display total
num = int(input('Enter a positive number: '))
while num > 0:
    total += num
    num = int(input('enter another number'))
    if num < 0:
        print('your sum is', total)
    
