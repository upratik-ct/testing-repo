from flask import Flask, jsonify, request
from app.db import tasks, add_task, delete_task, update_task

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

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

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    deleted = delete_task(task_id)
    return jsonify(deleted)

if __name__ == '__main__':
    app.run(debug=True)
