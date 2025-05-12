# A program where you can add tasks, view tasks, and remove completed tasks.
import time

tasks = []

def show_menu():
    print("\nTo-do lis menu: ")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. mark task as completed")
    print("5. Exit\n")

def view_tasks():
    if not tasks:
        time.sleep(0.3)
        print("No tasks yet!")
    else:
        time.sleep(1)
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{i}. {status} {task['text']}")

def add_task():
    new_task = input("Add a new task: ")
    tasks.append({"text": new_task, "done": False})
    time.sleep(1)
    print("Task added!")

def remove_task():
        time.sleep(0.3)
        view_tasks()
        try:
            time.sleep(1)
            delete_task = int(input("Enter the number of the task you want to delete: "))
            if 1 <= delete_task <= len(tasks):
                removed = tasks.pop(delete_task - 1)
                time.sleep(1)
                print(f"Removed: {removed}")
            else:
                print("invalid task number")
        except ValueError:
            print("Please enter a valid number.")

def mark_task_as_completed():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter the number of the task you want to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"]=True
            print(f"{num}. task is marked as completed.")
        else:
            print("invalid number.")
    except ValueError:
        print("Please enter a valid number.")



while True:
    show_menu()
    try:
        choice = int(input("Choose an option (1-4): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        view_tasks()

    elif choice == 2:
        add_task()

    elif choice == 3:
        remove_task()

    elif choice == 4:
        mark_task_as_completed()

    elif choice == 5:
        print("Goodbye. Have a great day!")
        break