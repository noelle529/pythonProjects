myPet = ['Kida', 'Skippy','grace']
print('Enter pet name:')
name = input()
if name not in myPet:
    print('I do not have a pet named ' + name)
else: 
    print(name + ' is my pet.')

