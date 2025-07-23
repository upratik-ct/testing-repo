---
title: Documentation for Models
---
# Introduction

This document will walk you through the implementation of the <SwmToken path="/app/models.py" pos="1:2:2" line-data="class Task:">`Task`</SwmToken> model in the application.

The <SwmToken path="/app/models.py" pos="1:2:2" line-data="class Task:">`Task`</SwmToken> model is designed to represent tasks with an ID, title, and completion status. It provides a method to convert the task instance into a dictionary format, which is useful for serialization and data manipulation.

We will cover:

1. Why the <SwmToken path="/app/models.py" pos="1:2:2" line-data="class Task:">`Task`</SwmToken> model is structured with specific attributes.
2. The purpose of the <SwmToken path="/app/models.py" pos="7:3:3" line-data="    def to_dict(self):">`to_dict`</SwmToken> method in the <SwmToken path="/app/models.py" pos="1:2:2" line-data="class Task:">`Task`</SwmToken> model.

# Task model structure

<SwmSnippet path="/app/models.py" line="1">

---

The <SwmToken path="/app/models.py" pos="1:2:2" line-data="class Task:">`Task`</SwmToken> model is structured with three attributes: <SwmToken path="/app/models.py" pos="2:8:8" line-data="    def __init__(self, id: int, title: str, completed: bool = False):">`id`</SwmToken>, <SwmToken path="/app/models.py" pos="2:14:14" line-data="    def __init__(self, id: int, title: str, completed: bool = False):">`title`</SwmToken>, and <SwmToken path="/app/models.py" pos="2:20:20" line-data="    def __init__(self, id: int, title: str, completed: bool = False):">`completed`</SwmToken>. This design decision allows each task to have a unique identifier (<SwmToken path="/app/models.py" pos="2:8:8" line-data="    def __init__(self, id: int, title: str, completed: bool = False):">`id`</SwmToken>), a descriptive name (<SwmToken path="/app/models.py" pos="2:14:14" line-data="    def __init__(self, id: int, title: str, completed: bool = False):">`title`</SwmToken>), and a boolean flag (<SwmToken path="/app/models.py" pos="2:20:20" line-data="    def __init__(self, id: int, title: str, completed: bool = False):">`completed`</SwmToken>) indicating whether the task is finished. This structure is essential for managing tasks effectively within the application.

```
class Task:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

```

---

</SwmSnippet>

# Purpose of the <SwmToken path="/app/models.py" pos="7:3:3" line-data="    def to_dict(self):">`to_dict`</SwmToken> method

<SwmSnippet path="/app/models.py" line="1">

---

The <SwmToken path="/app/models.py" pos="7:3:3" line-data="    def to_dict(self):">`to_dict`</SwmToken> method in the <SwmToken path="/app/models.py" pos="1:2:2" line-data="class Task:">`Task`</SwmToken> model is implemented to facilitate the conversion of a task instance into a dictionary format. This is particularly useful for serialization, enabling easy transformation of task data into JSON or other formats required for API responses or data storage. It ensures that the task's attributes are accessible in a structured manner.

```
class Task:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

```

---

</SwmSnippet>

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBdGVzdGluZy1yZXBvJTNBJTNBdXByYXRpay1jdA==" repo-name="testing-repo"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
