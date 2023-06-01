import sys

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        userInput = input('What task are you adding? ')
        self.tasks.append(userInput)
        print('Task added')

    def remove_task(self):
        remove_task = input('What task are you removing? Remember spelling counts!!! ')
        if remove_task in self.tasks:
            self.tasks.remove(remove_task)
            print('Task removed')
        else:
            print('Task not found')

    def display_tasks(self):
        print("To-Do List:")
        for display in self.tasks:
            print("- " + display)

    def to_do(self):
        print('''
        1 = Add task
        2 = Remove task
        3 = Display tasks
        4 = Exit program''')
        ask_user = input('Select an option: ')
        menu_options = {
            '1': self.add_task,
            '2': self.remove_task,
            '3': self.display_tasks,
            '4': sys.exit
        }

        try:
            menu_options.get(ask_user, lambda: print('Invalid option'))()
        except Exception as e:
            print('An error occurred:', str(e))

    def start(self):
        while True:
            self.to_do()

if __name__ == '__main__':
    todo_list = ToDoList()
    todo_list.start()


