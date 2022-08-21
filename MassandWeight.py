#Prompt user to enter object's mass
mass = int(input("enter object's mass"))

#Calculate the weight of the object
weight = mass * 9.8
print(weight, 'newtons')

#create if statement that will display
#whether or not the object is too heavy
#or if it is too light.
if weight < 100:
    print('The object is too light')
if weight > 500:
    print('The object is too heavy')
