---
title: Testing
---
# Introduction

This document will walk you through the implementation of task management endpoints in a Flask application. The purpose is to provide a clear understanding of how tasks are handled via HTTP requests.

We will cover:

1. How tasks are retrieved from the database.
2. How new tasks are created and added to the database.
3. How existing tasks are updated.
4. How tasks are deleted from the database.

# Retrieving tasks

<SwmSnippet path="/app/main.py" line="1">

---

The <SwmToken path="/app/main.py" pos="7:2:2" line-data="def get_tasks():">`get_tasks`</SwmToken> function is responsible for fetching all tasks from the database. This is achieved through a simple GET request to the <SwmToken path="/app/main.py" pos="6:6:7" line-data="@app.route(&#39;/tasks&#39;, methods=[&#39;GET&#39;])">`/tasks`</SwmToken> endpoint. The function returns a JSON representation of the tasks, making it easy to consume by clients.

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

# Creating tasks

<SwmSnippet path="/app/main.py" line="10">

---

The <SwmToken path="/app/main.py" pos="11:2:2" line-data="def create_task():">`create_task`</SwmToken> function handles the creation of new tasks. It listens for POST requests at the <SwmToken path="/app/main.py" pos="10:6:7" line-data="@app.route(&#39;/tasks&#39;, methods=[&#39;POST&#39;])">`/tasks`</SwmToken> endpoint. The function extracts the task details from the request's JSON payload and uses the <SwmToken path="/app/main.py" pos="13:5:5" line-data="    task = add_task(data.get(&#39;title&#39;, &#39;&#39;), data.get(&#39;completed&#39;, False))">`add_task`</SwmToken> function to store it in the database. A successful creation returns the task data with a 201 status code.

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

# Updating tasks

<SwmSnippet path="/app/main.py" line="10">

---

The <SwmToken path="/app/main.py" pos="17:2:2" line-data="def edit_task(task_id):">`edit_task`</SwmToken> function allows for updating existing tasks. It is triggered by PUT requests to the <SwmToken path="/app/main.py" pos="16:6:12" line-data="@app.route(&#39;/tasks/&lt;int:task_id&gt;&#39;, methods=[&#39;PUT&#39;])">`/tasks/<int:task_id>`</SwmToken> endpoint. The function updates the task's title and completion status based on the provided JSON data, utilizing the <SwmToken path="/app/main.py" pos="19:5:5" line-data="    updated = update_task(task_id, data.get(&#39;title&#39;), data.get(&#39;completed&#39;))">`update_task`</SwmToken> function.

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

# Deleting tasks

<SwmSnippet path="/app/main.py" line="22">

---

The <SwmToken path="/app/main.py" pos="23:2:2" line-data="def remove_task(task_id):">`remove_task`</SwmToken> function is designed to delete tasks. It responds to DELETE requests at the <SwmToken path="/app/main.py" pos="22:6:12" line-data="@app.route(&#39;/tasks/&lt;int:task_id&gt;&#39;, methods=[&#39;DELETE&#39;])">`/tasks/<int:task_id>`</SwmToken> endpoint. The function calls <SwmToken path="/app/main.py" pos="24:5:5" line-data="    deleted = delete_task(task_id)">`delete_task`</SwmToken> to remove the specified task from the database and returns the result as JSON.

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

# Running the application

<SwmSnippet path="/app/main.py" line="22">

---

Finally, the application is set to run in debug mode, which is useful for development and testing purposes. This allows for real-time feedback and error tracking during the development process.

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

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBdGVzdGluZy1yZXBvJTNBJTNBdXByYXRpay1jdA==" repo-name="testing-repo"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
