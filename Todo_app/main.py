# main.py
from todo_operations import add_task, delete_task, view_tasks
from utils import clear_screen, get_user_input

def display_menu():
    """Displays the menu for the user."""
    print("\n--- To-Do List Menu ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")

def main():
    """Main function to handle user interaction."""
    while True:
        clear_screen()
        display_menu()

        choice = get_user_input("Choose an option (1/2/3/4): ")

        if choice == '1':
            task = get_user_input("Enter a new task: ")
            add_task(task)

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            view_tasks()  # Show tasks before asking for index
            try:
                index = int(get_user_input("Enter the task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
