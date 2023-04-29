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
    x = float(a) * r + float(r2) # total of intial amount + rate

    total = pow(x,float(t)) #this variable returns the base raise to the power of exponent.
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

calculatorApp()