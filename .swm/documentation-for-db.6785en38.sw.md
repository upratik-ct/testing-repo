---
title: Documentation for DB
---
# Introduction

This document will walk you through the design decisions behind the task management functionality in the database module.

The purpose of this module is to handle task creation, updating, and deletion in a simple in-memory database.

We will cover:

1. How tasks are added and managed.
2. How tasks are updated.
3. How tasks are deleted.

# Adding tasks

<SwmSnippet path="/app/db.py" line="1">

---

The <SwmToken path="/app/db.py" pos="4:2:2" line-data="def add_task(title, completed=False):">`add_task`</SwmToken> function is responsible for creating new tasks. It uses a global <SwmToken path="/app/db.py" pos="2:0:0" line-data="next_id = 1">`next_id`</SwmToken> to ensure each task has a unique identifier. This approach allows us to easily track tasks without relying on external systems or databases.

```
tasks = []
next_id = 1

def add_task(title, completed=False):
    global next_id
    task = {"id": next_id, "title": title, "completed": completed}
    tasks.append(task)
    next_id += 1
    return task
```

---

</SwmSnippet>

# Updating tasks

<SwmSnippet path="/app/db.py" line="11">

---

The <SwmToken path="/app/db.py" pos="11:2:2" line-data="def update_task(task_id, title=None, completed=None):">`update_task`</SwmToken> function allows modification of existing tasks. It checks for the task by its unique identifier and updates the title or completion status if provided. This ensures that tasks can be dynamically modified based on user input or system requirements.

```
def update_task(task_id, title=None, completed=None):
    for task in tasks:
        if task["id"] == task_id:
            if title is not None:
                task["title"] = title
            if completed is not None:
                task["completed"] = completed
            return task
    return {"error": "Task not found"}
```

---

</SwmSnippet>

# Deleting tasks

<SwmSnippet path="/app/db.py" line="21">

---

The <SwmToken path="/app/db.py" pos="21:2:2" line-data="def delete_task(task_id):">`delete_task`</SwmToken> function removes tasks from the list based on their unique identifier. It filters out the task to be deleted and returns a confirmation message. This is crucial for maintaining an accurate list of tasks and freeing up resources.

```
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {"message": "Task deleted", "task_id": task_id}
```

---

</SwmSnippet>

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBdGVzdGluZy1yZXBvJTNBJTNBdXByYXRpay1jdA==" repo-name="testing-repo"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
