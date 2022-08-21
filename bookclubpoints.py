#ask user to enter number of books purchased
books = int(input('enter number of books purchased'))

if books == 0 or books < 2:
    print('You have earned 0 points')
if books >= 2 and books < 4:
    print('you have earned 5 points')
if books >= 4 and books < 6:
    print('you have earned 15 points')
if books >= 6 and books < 8:
    print('you have earned 30 points')
if books >= 8:
    print('you have earned 60 points')
