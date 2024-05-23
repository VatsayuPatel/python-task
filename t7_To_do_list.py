class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Added task : {task}')
        print(f'Task "{task}" added successfully..!!')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Remove task : {task}")
            print(f'Task "{task}" Remove successfully..!!')
        else:
            print(f"{task} Not Found")

    def view_task(self):
        print("To-do List : ")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")


def main():
    to_do_list = ToDoList()
    while True:
        print("\nWhat you want to do")
        print('1. Add Task')
        print('2. Remove a task')
        print('3. view all task')
        print('4. Exit')

        choice = input("Enter Choice : ")

        if choice == '1':
            task = input("Enter a new task ")
            to_do_list.add_task(task)

        elif choice == '2':
            task = input("Enter task which you want remove : ")
            to_do_list.remove_task(task)

        elif choice == '3':
            to_do_list.view_task()

        elif choice == '4':
            print("Exiting the To-Do List Manager. Goodbye!!")
            break

        else:
            print("Invalid Choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
