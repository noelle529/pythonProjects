#currency converter: make it your own
#other countries converted to use
""" pesos = 233.0 #colombia
reais = 244.0 #brazil
soles = 2220.0 #Peru
yen = 55.0 #japan """
def converstion():
    pesos = float(input('How much Pesos do you have? ')) #this automatically turn this input into a float and retun an error if not used properly
    reais = float(input('How much Reais do you have? '))
    soles = float(input('How much Soles do you have? '))
    yen = float(input('How much Yen do you have? '))

    total = float

    total = 0.000252 * pesos + 0.194370 * reais + 0.268531 * soles + 0.007339  * yen

    if total < 999.0:
        print('yooo you stayed under budget!!!!: ' + str(total))
    else: 
        print('Foreign Money Total = ' + str(total))

converstion()