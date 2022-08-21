speed = int(input('What is the speed travelled in mph?'))
hour = int(input('How hours did you travel?'))

print('HOUR\tDISTANCE TRAVELLED')
print('------------------------')

for number in range(1, hour + 1, 1):
    distance = speed * number
    print(number, '\t', distance)
