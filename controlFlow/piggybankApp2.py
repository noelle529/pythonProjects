#currency converter: make it your own
#other countries converted to use

pesos = 233.0 #colombia
reais = 244.0 #brazil
soles = 2220.0 #Peru
yen = 55.0 #japan

total = float

total = 0.000252 * pesos + 0.194370 * reais + 0.268531 * soles + 0.007339  * yen

if total < 999.0:
    print('yooo you stayed under budget!!!!')
else: 
    print("Foreign Money Total = " + total)