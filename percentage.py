males = int(input('enter number of males'))
females = int(input('enter number of females'))
total_students = males + females
percent_males = males / total_students
percent_females = females / total_students

print('the males in the class take up', (format(percent_males, '.0%')))
print('the females in the class take up', (format(percent_females, '.0%')))
