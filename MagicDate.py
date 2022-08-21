#prompt user to enter day, month, and year
day = int(input('enter the day of the month'))
month = int(input('enter the month of the year'))
year = int(input('enter the year'))

#calculate whether the day multiplied
#by the month equals the year.
if day * month == year:
    print('the date is magic')
else:
    print('the date is not magic')
