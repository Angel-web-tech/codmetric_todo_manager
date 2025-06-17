import os

TASK_FILE = "tasks.txt"

# Load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "done": status == "done"})
    return tasks

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            status = "done" if task["done"] else "pending"
            file.write(f"{task['task']}|{status}\n")

# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("📝 No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

# Add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("✅ Task added.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Task '{removed['task']}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Enter a valid number.")

# Mark task as completed
def mark_done(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"✅ Task '{tasks[index]['task']}' marked as completed.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Enter a valid number.")

# Main menu loop
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("📁 Tasks saved. Exiting...")
            break
        else:
            print("❌ Invalid choice. Please select from 1 to 5.")

# Run the program
if __name__ == "__main__":
    main()
