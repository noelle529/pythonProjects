def Grades(name):
    grade1 = input('what is your first grade?')
    grade2 = input('what is your second grade?')
    grade3 = input('what is your third grade?')
    grade4 = input('what is your forth grade?')
    grade5 = input('what is your fifth grade?')

    gradeAverage = float(grade1)+float(grade2)+float(grade3)+float(grade4)+float(grade5)

    sum = gradeAverage / 5
    if sum >= 100:
        print('your grade is an A ' + name +'!')
    else:
        print('Your grade is: '+ str(sum) + name)

Grades('Noelle') 













#note to self, indenting is very important. always check formatting when copying and pasting code