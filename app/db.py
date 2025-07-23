tasks = []
next_id = 1

def add_task(title, completed=False):
    global next_id
    task = {"id": next_id, "title": title, "completed": completed}
    tasks.append(task)
    next_id += 1
    return task

def update_task(task_id, title=None, completed=None):
    for task in tasks:
        if task["id"] == task_id:
            if title is not None:
                task["title"] = title
            if completed is not None:
                task["completed"] = completed
            return task
    return {"error": "Task not found"}

def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {"message": "Task deleted", "task_id": task_id}
