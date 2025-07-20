def task():
    tasks = []  # empty list

    print("----WELCOME TO THE TASK MANAGEMENT APP----")
    total_task = int(input("Enter how many tasks you want to add = "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"\nToday's tasks are:\n{tasks}\n")

    while True:
        operation = int(input("Choose an operation:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nYour choice: "))

        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.\n")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                new_task = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = new_task
                print(f"Task '{updated_val}' has been updated to '{new_task}'.\n")
            else:
                print("Task not found!\n")

        elif operation == 3:
            delete_val = input("Enter the task name you want to delete = ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"Task '{delete_val}' has been deleted.\n")
            else:
                print("Task not found!\n")

        elif operation == 4:
            print(f"\nCurrent tasks: {tasks}\n")

        elif operation == 5:
            print("Exiting the Task Management App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    task()
