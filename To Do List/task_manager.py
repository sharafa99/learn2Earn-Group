import main

def id_generator(tasks):
    
    if len(tasks) == 0:
        return 1
    else:
        id_list = map(int, tasks.keys())
        return max(id_list) + 1

def add_task(new_task, tasks):
    modified_tasks = {}
    modified_tasks.update(tasks)
    task_id = id_generator(tasks)
    modified_tasks[task_id] = new_task
    return modified_tasks

def delete_task(tasks, task_id):
    modified_tasks = {}
    modified_tasks.update(tasks)

    if task_id in modified_tasks:
        deleted_task = modified_tasks.pop(task_id)
        deleted = True
    else:
        deleted_task = None
        deleted = False

    return modified_tasks, deleted_task, deleted

def mark_task(task_id, tasks):
    new_tasks = {}
    new_tasks.update(tasks)

    if tasks[task_id]["Completed"]:
        return new_tasks, False

    new_tasks[task_id] = tasks[task_id].copy()
    new_tasks[task_id]["Completed"] = True

    return new_tasks, True

























# import models

# title = "Learning Python"
# priority = "High"
# due_date = None

# tasks = {}


# new_task = add_task(title, priority, tasks, due_date)

# print(f"Original task dictionary {tasks}")
# print(f"New task dictionary {new_task}")

# new_tasks, deleted = delete_task(tasks, 99)
# print(new_tasks)
# print(deleted)