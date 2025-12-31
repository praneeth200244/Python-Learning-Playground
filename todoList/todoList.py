taskList = []

def addTask():
    task = input("Please enter the task: ")
    taskList.append(task)
    print(f"{task} added successfully!")

def removeTask():
    if not taskList:
        print("No tasks to remove.")
        return

    displayTasks()
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        removed = taskList.pop(index)
        print(f"{removed} removed successfully!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def updateTask():
    if not taskList:
        print("No tasks to update.")
        return

    displayTasks()
    try:
        index = int(input("Enter the task number to update: ")) - 1
        new_task = input("Enter the new task: ")
        old_task = taskList[index]
        taskList[index] = new_task
        print(f"'{old_task}' updated to '{new_task}'!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def displayTasks():
    print("\nYour Tasks:")
    for i, task in enumerate(taskList, start=1):
        print(f"{i}. {task}")
    print()

def displayOptions():
    while True:
        print(
            "\nPlease select one of the below options."
            "\n1. Add a task"
            "\n2. Remove a task"
            "\n3. Update a task"
            "\n4. View tasks"
            "\n5. Exit"
        )

        option = input("Enter your choice: ")

        if option == '1':
            addTask()
        elif option == '2':
            removeTask()
        elif option == '3':
            updateTask()
        elif option == '4':
            displayTasks()
        elif option == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    displayOptions()
