def display_todo_list(todo_list):
    if todo_list:
        print("Your To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")
def main():
    todo_list = []

    while True:
        print("\nTo-Do List Menu:")
        print("1. Show Task List")
        print("2. Add a Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.append(task)
            print(f"Task '{task}' added to the To-Do List.")
        elif choice == '3':
            if todo_list:
                index = int(input("Enter the index of the task to remove: "))
                if 1 <= index <= len(todo_list):
                    task = todo_list.pop(index - 1)
                    print(f"Task '{task}' removed from the To-Do List.")
                else:
                    print("Invalid task index.")
            else:
                print("Your To-Do List is already empty.")
        elif choice == '4':
            print("Thank you for using the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()