#while loop test code
#password: bio324
while True:
    print('Who are You?')
    name = input()
    if name != 'Noelle':
        continue
    print('Hello Noelle, What is the password?')
    password = input()
    if password != 'bio324':
        print('Access Granted')