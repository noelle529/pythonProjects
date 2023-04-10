#temperature conversion
askTempC = input('What is the temperture in Celsius?')

fahrenheit = (float(askTempC)* 1.8) + 32 #is this convert celsius to fahrenheit


if float(askTempC) >= 1.0:
    print(fahrenheit)
elif float(askTempC) == 0.0: 
    askTempF = input('What is the temperture in Fahrenheit?')
    celsius = (float(askTempF)-32) / 1.8 #this is for converting fahrenheit to celsius
    print(celsius)



