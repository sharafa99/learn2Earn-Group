
def create_task(date_created, title, priority, due_date):
    
    to_do_data = {}

    to_do_data["Date Created"] = date_created
    to_do_data["Title"] = title
    to_do_data["Priority"] = priority
    to_do_data["Due Date"] = due_date
    to_do_data["Completed"] = False

    return to_do_data
