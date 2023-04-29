# grade average calculator app
name = input('What is your name?')
grade1 = float(input('what is your first grade?'))
grade2 = float(input('what is your second grade?'))
grade3 = float(input('what is your third grade?'))
grade4 = float(input('what is your forth grade?'))
grade5 = float(input('what is your fifth grade?'))

gradeAverage = grade1 + grade2 + grade3 + grade4 + grade5

sum = gradeAverage / 5
if sum >= 100:
    print('your grade is: A ' + name)
else:
    print('Your grade is:  '+ str(sum) +',' + name)
