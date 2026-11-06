import sys

# Initialize an empty list to store tasks. 
# Each task will be a dictionary: {"desc": "Task name", "completed": False}
tasks = []

def show_menu():
    print("\n" + "="*30)
    print("      📝 CLI TO-DO LIST")
    print("="*30)
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Mark Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")
    print("="*30)

def view_tasks():
    if not tasks:
        print("\n📥 Your to-do list is empty!")
        return
    
    print("\n📋 Current Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✅ Done" if task["completed"] else "❌ Pending"
        print(f"{idx}. [{status}] {task['desc']}")

def add_task():
    desc = input("\nEnter the task description: ").strip()
    if desc:
        tasks.append({"desc": desc, "completed": False})
        print(f"➕ Task '{desc}' added successfully!")
    else:
        print("⚠️ Task description cannot be empty.")

def complete_task():
    view_tasks()
    if not tasks:
        return
    try:
        choice = int(input("\nEnter the number of the task to mark complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            print(f"🏁 Task {choice} marked as completed!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        choice = int(input("\nEnter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"🗑️ Deleted task: '{removed['desc']}'")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\n👋 Goodbye! Thanks for staying organized.")
            sys.exit()
        else:
            print("⚠️ Invalid option, please try again.")

if __name__ == "__main__":
    main()
