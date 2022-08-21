#prompt user to enter number of packages
packages = int(input('enter number of packages'))

#define discount calculations
discount1 = packages * 0.10
discount2 = packages * 0.20
discount3 = packages * 0.30
discount4 = packages * 0.40

if packages >= 10 and packages <= 19:
    print('your discount amount is $', discount1)
if packages >= 20 and packages <= 49:
    print('your discount amount is $', discount2)
if packages >= 50 and packages <= 99:
    print('your discount amount is $', discount3)
if packages >= 100:
    print('your discount amount is $', discount4)
