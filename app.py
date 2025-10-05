from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 用一个简单的列表在内存中存储任务
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('content')
    if task_content:
        tasks.append({'id': len(tasks) + 1, 'content': task_content})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    # 重新分配ID
    for i, task in enumerate(tasks, start=1):
        task['id'] = i
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)