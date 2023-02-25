from flask import Flask

from Todo import Todo

app = Flask(__name__)

todo1: Todo = Todo(1, "Todo 1")
todo2: Todo = Todo(1, "Todo 2")
todo3: Todo = Todo(1, "Todo 3")
todo4: Todo = Todo(1, "Todo 4")
todos: list[Todo] = [todo1, todo2, todo3, todo4]


@app.route('/')
def main() -> str:
    message: str = '<h1>Hello on Todapp</h1>'
    message += "<ul>"
    for todo in todos:
        message += f"<li>[{todo.status.value}] {todo.title}</li>"
    message += "</ul>"
    return message


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
