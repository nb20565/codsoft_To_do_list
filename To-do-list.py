# Function to display the menu options
def display_menu():
    print("To-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

# Function to view the to-do list
def view_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print("Task added successfully.")

# Function to remove a task from the to-do list
def remove_task(todo_list):
    view_list(todo_list)
    if todo_list:
        try:
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            if 0 <= task_index < len(todo_list):
                removed_task = todo_list.pop(task_index)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a valid integer index.")
    else:
        print("Your to-do list is empty.")

# Function to mark a task as completed
def mark_completed(todo_list):
    view_list(todo_list)
    if todo_list:
        try:
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            if 0 <= task_index < len(todo_list):
                todo_list[task_index] += " (Completed)"
                print("Task marked as completed.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a valid integer index.")
    else:
        print("Your to-do list is empty.")

# Main function
def main():
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            remove_task(todo_list)
        elif choice == "4":
            mark_completed(todo_list)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()





















