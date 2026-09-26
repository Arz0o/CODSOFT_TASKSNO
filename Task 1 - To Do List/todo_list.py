tasks = []


def add_task():
    task = input("Enter the task: ")

    if task.strip() == "":
        print("Task cannot be empty.")
        return

    tasks.append({
        "task": task,
        "completed": False
    })

    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n========== TO-DO LIST ==========")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"{i}. {task['task']} - {status}")


def update_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to update: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        new_task = input("Enter the updated task: ")

        if new_task.strip() == "":
            print("Task cannot be empty.")
            return

        tasks[number - 1]["task"] = new_task

        print("Task updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to mark as completed: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        tasks[number - 1]["completed"] = True

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        deleted_task = tasks.pop(number - 1)

        print(f"Task '{deleted_task['task']}' deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n================================")
    print("          TO-DO LIST")
    print("================================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")
    print("================================")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        complete_task()

    elif choice == "5":
        delete_task()

    elif choice == "6":
        print("\nThank you for using the To-Do List!")
        break

    else:
        print("\nInvalid choice! Please enter a number from 1 to 6.")