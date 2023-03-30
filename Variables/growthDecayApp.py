a = input('what is the starting amount?') #the inital amount
r = 1.0  #rate calculation(growth) : to make DECAY change "addtion" symbol to "subtraction" 

r2 = input('what is the rate of growth or decay?')#rate of growth or decay can be changed
t = input('how long in years?') # time
x = float(a) * r + float(r2) # total of intial amount + rate

total = pow(x,float(t)) #this variable returns the base raise to the power of exponent.
print(total)


