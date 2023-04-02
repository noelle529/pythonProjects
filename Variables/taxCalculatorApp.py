#NYC sales tax calculator
salePrice = input('what is the price of the item?')
cityTax = float(salePrice) * 0.04
stateTax = float(salePrice) * 0.04

amtDue =  cityTax + stateTax + float(salePrice)
print('You owe: ' + str(amtDue))