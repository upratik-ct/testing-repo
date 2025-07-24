tasks = []
    """
    The above Python code defines functions to add, update, and delete tasks in a task list.
    
    :param title: The `title` parameter in the functions `add_task` and `update_task` represents the
    title or name of the task being added or updated in the task list. It is a string that describes the
    task to be performed
    :param completed: The `completed` parameter in the `add_task` function is a boolean parameter that
    indicates whether a task has been completed or not. By default, it is set to `False`, meaning the
    task is not completed when a new task is added, defaults to False (optional)
    :return: The functions `add_task`, `update_task`, and `delete_task` are being defined in the code
    snippet. When these functions are called, they perform the following actions:
    """

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
