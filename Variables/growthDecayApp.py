a = input('what is the starting amount?') #the inital amount
r = 1.0 + 0.1 #rate calculation(growth) : to make DECAY change "addtion" symbol to "subtraction"
t = input('how long in years?') # time
x = float(a) * r # total of intial amount + rate

total = pow(x,float(t)) #this variable returns the base raise to the power of exponent.
print(total)
