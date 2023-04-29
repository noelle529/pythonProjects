import sys
import cmath
""" a = 5.0
    b = -5.0
    c = 12.0 """
#this app allows the user to pick what math formula app they want to use either Slope app or Quadaric formula App
def quadApp():
    a = float(input('What is your A?'))
    b = float(input('What is your B?'))
    c = float(input('What is your C?'))
    root1 = 0.0
    root2 = 0.0

    #root1 = float((-b + (b*b - 4*a*c).sqrt()) / (2*a) )
    root1 = (-b+cmath.sqrt(b*b - 4*a*c)) / (2*a)
    root2 = (-b-cmath.sqrt(b*b - 4*a*c)) / (2*a)
    #root2 = float((-b - (b*b - 4*a*c).sqrt()) / (2*a) )

    print(root1)
    print(root2)

def slopeApp():
    xOne = input('What is the X one?')
    xTwo = input('What is the X two?')
    yOne = input('What is the Y one?')
    yTwo = input('What is the Y two?')

    total = (float(yTwo)-float(yOne))/(float(xTwo)- float(xOne))
    print(total)

def growth_decay_app():
    a = input('what is the starting amount?') #the inital amount
    r = 1.0  #rate calculation(growth) : to make DECAY change "addtion" symbol to "subtraction" 

    r2 = input('what is the rate of growth or decay?')#rate of growth or decay can be changed
    t = input('how long in years?') # time
    growth_decay = input('Do you want growth or decay?')
    print('Answer: G or D')
    x1 = float(a) * r + float(r2) # growth
    x2 = float(a) * r - float(r2) # decay
    if growth_decay == 'G':
        total = pow(x1,float(t))
    elif growth_decay == 'D':
        total = pow(x2,float(t))
    print(total)

def calculatorApp():
   
        print(''' 
            Slope App : '1'
            Quadaric: '2'
            Growth and decay: '3'
        ''')
        calc_again = input('''Which math formula do you want to use?''')
        if calc_again == '1':
            slopeApp()
        elif calc_again == ('2'):
            quadApp()
        elif calc_again == ('3'):
            growth_decay_app()
        else:
            calculatorApp()

        again = input('Do you want to run this program again?')
        print('Answer: Y ')
        if again == ('Y'.upper):
            calculatorApp()
        else:
            print('Goodbye, See you later')

calculatorApp()