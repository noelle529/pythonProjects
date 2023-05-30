a = input('what is the starting amount?') #the inital amount
r = 1.0  #rate calculation(growth) : to make DECAY change "addtion" symbol to "subtraction" 

r2 = input('what is the rate of growth or decay?')#rate of growth or decay can be changed
t = input('how long in years?') # time
growth_decay = input('Do you want growth or decay?')
print('Answer: G or D')
rate = float(r) + float(r2)
amount = float(a) * rate
# x1 = float(a) * r + float(r2) # growth
#x2 = float(a) * r - float(r2) # decay

if growth_decay == 'G':
    total = pow(amount,float(t))
elif growth_decay == 'D':
    total = pow(amount,float(t))
print(total)


