#prompt user to enter 2 primary colors
color_mix = input('enter your 2 primary colors: ')

#create if statement that displays the
#corresponding secondary color.

if color_mix == 'red and blue' or color_mix == 'blue and red':
    print('you get purple')
if color_mix == 'red and yellow' or color_mix == 'yellow and red':
    print('you get orange')
if color_mix == 'blue and yellow' or color_mix == 'yellow and blue':
    print('you get green')
