#curreny converter app
pound = 1.0
ukCurrency = input('what is the UK currency?')
canada = 1.0
canadaCurrency = input('what is the Canadian currency?')
euro = 1.0
euroCurrency = input('what is the Euro currency?')
yen = 0.8
yenCurrency = input('what is the Japanese currency?')
total = 0.0

total = float(ukCurrency) * pound + float(canadaCurrency) * canada + float(euroCurrency) * euro + float(yenCurrency) * yen 

print('US Dollars = $' + str(total))
