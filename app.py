from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data storage (replace with database in real applications)
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.json.get('task', '')
    if task:
        tasks.append(task)
        return jsonify({"status": "success", "tasks": tasks})
    return jsonify({"status": "error", "message": "Task cannot be empty"})

@app.route('/get_tasks')
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    