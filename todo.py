# A program where you can add tasks, view tasks, and remove completed tasks.
import time

tasks = []

def show_menu():
    print("\nTo-do lis menu: ")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit\n")


while True:
    show_menu()
    try:
        choice = int(input("Choose an option (1-4): "))
    except ValueError:
        print("Please enter a valid number.")
        continue


    if choice == 1:
        if not tasks:
            time.sleep(0.3)
            print("No tasks yet!")
        else:
            time.sleep(1)
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        pass


    elif choice == 2:
        new_task = input("Add a new task: ")
        tasks.append(new_task)
        time.sleep(1)
        print("Task added!")
        pass


    elif choice == 3:
        if not tasks:
            print("No tasks to remove.")
        else:
            time.sleep(1)
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        try:
            time.sleep(1)
            delete_task = int(input("Enter the number of the task you want to delete: "))
            if 1<= delete_task <= len(tasks):
                removed = tasks.pop(delete_task-1)
                time.sleep(1)
                print(f"Removed: {removed}")
            else:
                print("invalid task number")
        except ValueError:
            print("Please enter a valid number.")
            continue
        pass


    elif choice == 4:
        print("Goodbye. Have a great day!")
        break