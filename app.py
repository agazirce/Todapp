import sqlite3

from flask import Flask, render_template, redirect, request

from Todo import Todo

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def home():
    todos: list[Todo] = []
    co = sqlite3.connect('todo.db')
    cursor = co.cursor()
    cursor.execute("SELECT * FROM todos ORDER BY status, id DESC ;")
    rows = cursor.fetchall()
    cursor.close()
    co.close()

    for row in rows:
        todos.append(Todo(row[0], row[1], row[2], row[3]))
    return render_template("list.html", todos=todos)


@app.route('/change_into_done/<int:todo_id>')
def change_into_done(todo_id: int):
    params = ("done", f"{todo_id}")
    co = sqlite3.connect('todo.db')
    cursor = co.cursor()
    cursor.execute("UPDATE todos SET status=? WHERE id=? ;", params)
    co.commit()
    cursor.close()
    co.close()

    return redirect('/list')


@app.route('/detail/<int:todo_id>')
def detail(todo_id: int):
    params = (f"{todo_id}",)
    co = sqlite3.connect('todo.db')
    cursor = co.cursor()
    cursor.execute("SELECT * FROM todos WHERE id=? ;", params)
    row = cursor.fetchone()
    cursor.close()
    co.close()

    if not row:
        return redirect('/')

    todo: Todo = Todo(row[0], row[1], row[2], row[3])
    return render_template("detail.html", todo=todo)


@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    description = request.form.get('description')
    co = sqlite3.connect('todo.db')
    cursor = co.cursor()
    cursor.execute("INSERT INTO todos(title, description) VALUES(?, ?)", (todo, description))
    co.commit()
    cursor.close()
    co.close()
    return redirect('/')


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
