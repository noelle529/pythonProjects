import cmath
def quadApp():
    a = 5.0
    b = -5.0
    c = 12.0

    root1 = 0.0
    root2 = 0.0

    #root1 = float((-b + (b*b - 4*a*c).sqrt()) / (2*a) )
    root1 = (-b+cmath.sqrt(b*b - 4*a*c)) / (2*a)
    root2 = (-b-cmath.sqrt(b*b - 4*a*c)) / (2*a)
    #root2 = float((-b - (b*b - 4*a*c).sqrt()) / (2*a) )

    print(root1)
    print(root2)

def slopApp():
    xOne = input('What is the X one?')
    xTwo = input('What is the X two?')
    yOne = input('What is the Y one?')
    yTwo = input('What is the Y two?')

    total = (float(yTwo)-float(yOne))/(float(xTwo)- float(xOne))
    print(total)

def calculatorApp():
  


