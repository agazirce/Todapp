import sqlite3

from flask import Flask, render_template, redirect

from Todo import Todo

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def home():
    todos: list[Todo] = []
    co = sqlite3.connect('todo.db')
    cursor = co.cursor()
    cursor.execute("SELECT * FROM todos ORDER BY status, id")
    rows = cursor.fetchall()
    cursor.close()
    co.close()

    for row in rows:
        todos.append(Todo(row[0], row[1], row[2]))
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


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
