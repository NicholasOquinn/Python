#this program calculates the total
#number of bugs in 5 days

MAX = 5 #max number of days

#initialize accumulator variable
total = 0.0

#explain whats happening
print('this program calculate the sum of bugs')
print('over a span of 5 days')

#get the numbers and accumulate them.
for counter in range(MAX):
    bugs = int(input('enter number of bugs'))
    total += bugs

#display the total number of bugs
print('The total number of bugs is', total)
    
