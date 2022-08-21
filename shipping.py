#Prompt user to enter weight of package
weight = int(input('enter weight of package'))

#set up different charging situations 
charge1 = weight * 1.50
charge2 = weight * 3.00
charge3 = weight * 4.00
charge4 = weight * 4.75

#create if statement to determine shipping costs
#based on weight of package.
if weight <= 2:
    print('the shipping charges are $', charge1)
if weight > 2 and weight < 6:
    print('the shipping charges are $', charge2)
if weight > 6 and weight < 10:
    print('the shipping charges are $', charge3)
if weight > 10:
    print('the shipping charges are $', charge4)
    
             
