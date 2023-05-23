Noelle = ['purple','tarot cards','kingdom hearts']
teacher = [['science', 'biology','pizza','tea','section 6'],[1,2,3,4,5]]
#print('I am teacher and I teach: ' + teacher[0][1] + ' I also like to play video games and my favorite one is ' + Noelle[2]) 

#when something has two list use index number to select which list
if 'biology' in teacher[0]:  
    print('true')

#iterate over list   
for i in Noelle:
    print(i)

#practical use
supplies = ['pens', 'pencils','Scissors','post-it-notes','markers','crayons','rulers']
for supplyList in range(len(supplies)):
    print('Index: ' + str(supplyList) + ' in supplies list is: ' + supplies[supplyList])

#multiple assignments
color, magic, hobby = Noelle
print(color + magic + hobby)

catNames = []

while True:
    print('Enter the name of a cat' + str(len(catNames)+ 1) + '(Or enter nothing to stop)')
    name = input()
    if  name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are: ')
for name in catNames:
    print('   ' + name)

# loop supplies
# school supplies

supplies = ['pens', 'scissors','paper','binders','staplers']

for i in range(len(supplies)):
    print('Index: ' + str(i) + ' in supplies is: ' + supplies[i])

# is adding a ask to add supplies and add to current list