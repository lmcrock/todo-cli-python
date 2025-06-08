# todo_app.py

tasks = []

def show_menu():
    print("\n=== To-Do List Application ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task():
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: '{task}'")
    else:
        print("Task cannot be empty!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks()
    try:
        index = int(input("Enter the number of the task to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Deleted task: '{removed}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-4): ")
        try:
            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please choose from 1 to 4.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("-" * 40)

if __name__ == "__main__":
    main()
