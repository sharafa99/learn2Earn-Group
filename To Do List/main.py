import os
import sys
import time
import datetime
import storage
import models
import task_manager

def header(text):
    space = int((50-len(text))/2)
    print("="*50,)
    print(" "*space, end="")
    print(f"{text}")
    print("="*50)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_task(new_task):
    print("\n")
    print("="*110)
    print(f"| DATE{'':>10} | TITLE{'':>20} | PRIORITY{'':>10} | DUE DATE{'':>10} | COMPLETED{'':>10} |")
    print("|","="*106,"|", end="")
    print("")
    if new_task["Due Date"] == None:
        display_due_Date = "N/A"
    else:
        display_due_Date = new_task["Due Date"]

    if new_task["Completed"] == True:
        display_completed = "True"
    else:
        display_completed = "False"

    print(f"| {new_task["Date Created"]:<15}| {new_task["Title"]:<25} | {new_task["Priority"]:18} | {display_due_Date:<18} | {display_completed:<19} |")
    print("="*110)
    
    print("\n")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")

    else:
        print("="*125)
        print(f"| ID{'':>5} | DATE{'':>10} | TITLE{'':>30} | PRIORITY{'':>10} | DUE DATE{'':>7} | COMPLETED{'':>8} |")
        print("|","="*121,"|", end="")
        print("")

        for key in tasks:
            if tasks[key]["Due Date"] == None:
                display_due_Date = "N/A"
            else:
                display_due_Date = tasks[key]["Due Date"]

            if tasks[key]["Completed"] == True:
                display_completed = "True"
            else:
                display_completed = "False"
            

            print(f"| {key:<7} | {tasks[key]["Date Created"]:<15}| {tasks[key]["Title"]:<35} | {tasks[key]["Priority"]:<18} | {display_due_Date:<15} | {display_completed:<17} |")
        print("="*125)

def show_menu():
    clear_terminal()
    header("📝 CLI TO-DO LIST")
    print("\n")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Edit task")
    print("5. Delete task")
    print("6. Filter tasks")
    print("7. Exit")

def today_date():
    today_date = datetime.date.today()
    return today_date.strftime("%Y-%m-%d")

def due_date_generator():

    while True:
        date_text = input("Input your date here in the format (YYYY-MM-DD): ")
        try:
            converted_date = datetime.datetime.strptime(date_text, "%Y-%m-%d")
        except ValueError:
            print("Error: Please input a valid date")
            continue
        break

    task_due_date = converted_date.date()
    return task_due_date.strftime("%Y-%m-%d")

def main():
    tasks = storage.load_storage("tasks.json")
    
    while True:
        show_menu()
        print()
        while True:
            try:
                choice = int(input("Choose an option (1-7): ").strip())

            except ValueError:
                print("Error: Empty space and text are no allowed: ")
                continue

            if choice not in (1, 2, 3, 4, 5, 6, 7):
                print("Please choose option between (1-7)")
                continue
            break

        if choice == 1:

            clear_terminal()
            header("Add Task")
            print("\n")

            while True:
                try:
                    title = input("Please input a title for the task: ")
    
                    if not title.strip() or any(char.isdigit() for char in title):
                        raise ValueError("Invalid input! Numbers or empty text are not allowed.")
    
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
                break
            
            print("\n")

            while True:
                try:
                    priority = input('Plese enter "Low", "Medium" or "High" for the priority level: ').capitalize()
    
                    if not priority.strip() or any(char.isdigit() for char in priority):
                        raise ValueError("Invalid input! Numbers or empty text are not allowed.")
                    allowed_words = ["Low","Medium", "High"]
                    if priority not in allowed_words:
                        raise ValueError(f"Please choose from: {', '.join(allowed_words)}")
    
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
                break

            while True:
                try:
                    due_date_choice = input("Would you like to add a Due date to your task? (y/n)").lower()

                    if not due_date_choice.strip() or any(char.isdigit() for char in due_date_choice):
                        raise ValueError("Invalid input! Numbers or empty text are not allowed")

                    allowed_words = ["y", "n"]
                    if due_date_choice not in allowed_words:
                        raise ValueError(f"Please choose from: {', '.join(allowed_words)}")

                except ValueError as e:
                    print(f"Error: {e}")
                    continue

                break

            if due_date_choice == "y":
                date_created = today_date()
                due_date = due_date_generator()
            else:
                date_created = today_date()
                due_date = None

            new_task = models.create_task(date_created, title, priority, due_date)

            display_task(new_task)

            latest_tasks = task_manager.add_task(new_task, tasks)

            while True:
                try:
                    save_task = input("Would you like to save the above task (yes / no): ")
        
                    if not save_task.strip() or any(char.isdigit() for char in save_task):
                        raise ValueError("Invalid input! Numbers or empty text are not allowed.")
                    allowed_words = ["yes","no"]
                    if save_task.lower() not in allowed_words:
                        raise ValueError(f"Please choose from: {', '.join(allowed_words)}")
        
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
        
                break
    
            if save_task == "yes":
                tasks = latest_tasks
                storage.save_task(tasks, "tasks.json")
                print("\n")
                print(f"Success! Your task is saved successfully")
                time.sleep(2)
            else:
                print("\n")
                print("Your task is not saved")
                time.sleep(2)
            time.sleep(3)
        
        elif choice == 2:
            clear_terminal()
            header("View Tasks")
            print("\n")
            view_tasks(tasks)
            print("\n")
            while True:
                try:
                    back = input('Type "back" to return to the main menu: ').strip().lower()
        
                    if back != "back":
                        raise ValueError(f'Please type "back" when you are done viewing the expenses: ')
        
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
        
                break
        
        elif choice == 3:
            clear_terminal()
            header("Mark Task as Completed")
            print("\n")
            view_tasks(tasks)
            print("\n")

            while True:
                try:
                    task_completed_id = int(input("Enter the ID of the task you would like to mark as completed: ").strip())
                    
                except ValueError:
                    print("Please enter a number. ")
                    continue
                if not task_completed_id in tasks.keys():
                    print("Invalid task ID")
                    continue
                break

            modified_tasks, mark_task_report = task_manager.mark_task(task_completed_id, tasks)

            if not mark_task_report:
                print()
                print(f"The task with the ID {task_completed_id} has already been marked 'Completed'")
                time.sleep(5)
            else:
                tasks = modified_tasks
                storage.save_task(tasks, "tasks.json")
                print("Task updated successfully")
                time.sleep(5)
        
        elif choice == 4:
            clear_terminal()
            header("Edit Tasks")
            print("\n")
            view_tasks(tasks)
            print("\n")

            while True:
                try:
                    edit_task_id = int(input("Delete the task with the ID number: ").strip())
                    
                    if not edit_task_id:
                        raise ValueError("Invalid input! letters or empty space are not allowed.")

                    # if not deleted:
                    #     raise ValueError("Invalid ID number supplied ")
                        
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
    
                break

            print(f"The task choosen to be Deleted is :")
            display_task(task_deleted)

            time.sleep(3)
        
        elif choice == 5:
            clear_terminal()
            header("Delete Tasks")
            print("\n")
            view_tasks(tasks)
            print("\n")

            while True:
                try:
                    deleting_task_id = int(input("Delete the task with the ID number: ").strip())
                    
                    if not deleting_task_id:
                        raise ValueError("Invalid input! letters or empty space are not allowed.")
                    
                    refined_tasks, task_deleted, deleted = task_manager.delete_task(tasks, deleting_task_id)
                                        
                    if not deleted:
                        raise ValueError("Invalid ID number supplied ")
                        
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
    
                break

            print(f"The task choosen to be Deleted is :")
            display_task(task_deleted)
            while True:
                try:
                    final_delete = input(f"Are you sure you want to permanently delete the task with the ID number {deleting_task_id}? (y/n): ").lower()
        
                    if not final_delete.strip() or any(char.isdigit() for char in final_delete):
                        raise ValueError("Invalid input! Numbers or empty text are not allowed.")
                    allowed_words = ["y","n"]
                    if final_delete not in allowed_words:
                        raise ValueError(f"Please choose from: {', '.join(allowed_words)}")
        
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
        
                break
            if final_delete == "y":
                tasks = refined_tasks
                storage.save_task(tasks, "tasks.json")
                print("\n")
                print(f"Success! Your task is permanently deleted successfully")
                time.sleep(3)
            else:
                print("Task Deleting was not successful")
                time.sleep(5)
        
        elif choice == 6:
            print("Filter tasks selected")
            time.sleep(3)
        
        else:
            print("\n👋 Goodbye! Thanks for staying organized.")
            sys.exit()
                     
if __name__ == "__main__":
    main()