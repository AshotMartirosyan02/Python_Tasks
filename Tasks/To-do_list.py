def display_tasks(tasks):
    if not tasks:
        print("\nTask not in list.")
    else:
        print("\nList:")
        for task_id, task in tasks.items():
            status = "Completed" if task["completed"] else "Not completed"
            print(f"Uniq ID {task_id}.  {task['task_inp']}, mode: {task['mode']} --> {status}")

def add_task(tasks, id):
    task_inp = input("Enter a task: ").strip()
    if not task_inp:
        print("Task  cannot be empty.")
        return id

    mode = input("Enter task mode (low, medium, high): ").lower()
    if mode not in ["low", "medium", "high"]:
        print("Invalid input:  Setting to low.")
        mode = "low"

    tasks[id] = {
        "task_inp": task_inp,
        "completed": False,
        "mode": mode
    }
    print("Task added.")
    return id + 1

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    display_tasks(tasks)
    task_id = int(input("Enter task ID to remove: "))
    if task_id in tasks:
        del tasks[task_id]
        print("Task removed.")
    else:
        print("Invalid task ID.")

def mark_task(tasks):
    display_tasks(tasks)
    task_id = int(input("Enter the task ID:  "))
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task ID.")

def list_completed_tasks(tasks):
    completed_tasks = {id: task for id, task in tasks.items() if task["completed"]}
    display_tasks(completed_tasks)


def main_foo():
    tasks = {}
    id = 1

    while True:
        print("\nadd, remove, show, complete, show_completed, quit")
        choice = input("Enter your choice: ").lower()

        if choice == "add":
            id = add_task(tasks, id)
        elif choice == "remove":
            remove_task(tasks)
        elif choice == "show":
            display_tasks(tasks)
        elif choice == "complete":
            mark_task(tasks)
        elif choice == "show_completed":
            list_completed_tasks(tasks)
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_foo()