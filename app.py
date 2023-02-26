import sqlite3

from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
