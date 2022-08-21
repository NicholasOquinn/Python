#Ask user to enter age
Age = int(input('Enter age'))

#Create if statement determining
#whether the person is an infant,
#child, teenager, or an adult.
if Age <= 1:
    print('This person is an infant')
if Age > 1 and Age < 13:
    print('This person is a child')
if Age >= 13 and Age < 20:
    print('This person is a teenager')
if Age >= 20:
    print('this person is an adult')
