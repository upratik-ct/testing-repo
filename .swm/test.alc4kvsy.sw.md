---
title: Test
---
# Introduction

This document will walk you through the implementation of a simple task management API using Flask. The API allows for creating, retrieving, updating, and deleting tasks.

We will cover:

1. How the API endpoints are structured and their purpose.
2. The flow of data through the application.
3. The rationale behind the design choices made in the implementation.

# Code flow

## Retrieving tasks

<SwmSnippet path="/app/main.py" line="1">

---

The <SwmToken path="/app/main.py" pos="6:6:7" line-data="@app.route(&#39;/tasks&#39;, methods=[&#39;GET&#39;])">`/tasks`</SwmToken> endpoint is defined to handle GET requests. This endpoint is responsible for retrieving the list of tasks from the database. The function <SwmToken path="/app/main.py" pos="7:2:2" line-data="def get_tasks():">`get_tasks`</SwmToken> returns the tasks in JSON format, making it easy for clients to consume.

```
from flask import Flask, jsonify, request
from app.db import tasks, add_task, delete_task, update_task

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)
```

---

</SwmSnippet>

## Creating and updating tasks

<SwmSnippet path="/app/main.py" line="10">

---

The <SwmToken path="/app/main.py" pos="10:6:7" line-data="@app.route(&#39;/tasks&#39;, methods=[&#39;POST&#39;])">`/tasks`</SwmToken> endpoint also handles POST requests for creating new tasks. The <SwmToken path="/app/main.py" pos="11:2:2" line-data="def create_task():">`create_task`</SwmToken> function extracts task details from the request and uses the <SwmToken path="/app/main.py" pos="13:5:5" line-data="    task = add_task(data.get(&#39;title&#39;, &#39;&#39;), data.get(&#39;completed&#39;, False))">`add_task`</SwmToken> function to add it to the database. It returns the newly created task with a 201 status code, indicating successful creation.

```
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = add_task(data.get('title', ''), data.get('completed', False))
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def edit_task(task_id):
    data = request.json
    updated = update_task(task_id, data.get('title'), data.get('completed'))
    return jsonify(updated)
```

---

</SwmSnippet>

The same snippet also defines the <SwmToken path="/app/main.py" pos="16:6:12" line-data="@app.route(&#39;/tasks/&lt;int:task_id&gt;&#39;, methods=[&#39;PUT&#39;])">`/tasks/<int:task_id>`</SwmToken> endpoint for PUT requests, which is used to update existing tasks. The <SwmToken path="/app/main.py" pos="17:2:2" line-data="def edit_task(task_id):">`edit_task`</SwmToken> function updates the task details in the database using the <SwmToken path="/app/main.py" pos="2:17:17" line-data="from app.db import tasks, add_task, delete_task, update_task">`update_task`</SwmToken> function and returns the updated task.

## Deleting tasks

<SwmSnippet path="/app/main.py" line="22">

---

The <SwmToken path="/app/main.py" pos="22:6:12" line-data="@app.route(&#39;/tasks/&lt;int:task_id&gt;&#39;, methods=[&#39;DELETE&#39;])">`/tasks/<int:task_id>`</SwmToken> endpoint handles DELETE requests. The <SwmToken path="/app/main.py" pos="23:2:2" line-data="def remove_task(task_id):">`remove_task`</SwmToken> function deletes the specified task from the database using the <SwmToken path="/app/main.py" pos="24:5:5" line-data="    deleted = delete_task(task_id)">`delete_task`</SwmToken> function and returns the result in JSON format. This ensures that tasks can be removed when no longer needed.

```
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    deleted = delete_task(task_id)
    return jsonify(deleted)

if __name__ == '__main__':
    app.run(debug=True)
```

---

</SwmSnippet>

# Conclusion

The design of this API is straightforward, focusing on CRUD operations for task management. Each endpoint is clearly defined to handle specific HTTP methods, ensuring a clean separation of concerns. The use of Flask allows for a simple yet effective way to manage tasks, making it easy to extend or modify as needed.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBdGVzdGluZy1yZXBvJTNBJTNBdXByYXRpay1jdA==" repo-name="testing-repo"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
