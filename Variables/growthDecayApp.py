a = input('what is the starting amount?') #the inital amount
r = 1.0  #rate calculation(growth) : to make DECAY change "addtion" symbol to "subtraction" 

r2 = input('what is the rate of growth or decay?')#rate of growth or decay can be changed
t = input('how long in years?') # time
growth_decay = input('Do you want growth or decay?')
print('Answer: G or D')
x1 = float(a) * r + float(r2) # total of intial amount + rate (growth)
x2 = float(a) * r - float(r2) # decay

# total = pow(x,float(t)) #this variable returns the base raise to the power of exponent.
if growth_decay == 'G':
    total = pow(x1,float(t))
elif growth_decay == 'D':
    total = pow(x2,float(t))

print(total)


