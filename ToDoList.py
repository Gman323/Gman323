tasks = []

def add_task(task):
  tasks.append(task)

def complete_task(index):
  tasks.pop(index)

def list_tasks():
  for i, task in enumerate(tasks):
    print(f'{i+1}. {task}')

def run_todo_list():
  while True:
    action = input('What would you like to do? (add/complete/list/quit) ')
    if action == 'add':
      task = input('Enter a task: ')
      add_task(task)
    elif action == 'complete':
      index = int(input('Enter the index of the task to complete: ')) - 1
      complete_task(index)
    elif action == 'list':
      list_tasks()
    elif action == 'quit':
      break
    else:
      print('Invalid input. Try again.')

run_todo_list()
