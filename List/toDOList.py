#to-do list
import sys

tasks = []

#function to add task
def addTask():
	userInput = input('What task are you adding?')
	tasks.append(userInput)
	print('Task added')

#function for removing tasks
def removeTask():
    remove_task = input('What task are you removing? Remember spelling counts!!! ')
    if remove_task in tasks:
        tasks.remove(remove_task)
        print('Task removed')
    else:
        print('Task not found')

#funtion to display tasks
def displayTask():
	for display in tasks:
		print("To-Do List: " + display)

#function for todo list
def toDo():
	print('''
	1 = add task
	2 = remove task
	3 = display tasks
	4 = End program''')
	askUser = input('')
	if askUser == '1':
		addTask()
	elif askUser == '2':
		removeTask()
	elif askUser == '3':
		displayTask()
	elif askUser == '4':
		sys.exit()
		
while True:
	try:
		toDo()
	except:
		print('Sorry you have encountered an error, please try again later.')
