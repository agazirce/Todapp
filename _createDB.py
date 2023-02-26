import sqlite3

co = sqlite3.connect('todo.db')
cursor = co.cursor()

# CREATE DB
cursor.execute(
    "CREATE TABLE IF NOT EXISTS todos("
    "   id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT, status TEXT DEFAULT 'current') ;")

# INSERT EXEMPLE
t = ("Todo 1", 'This is a beautifull tasks')
cursor.execute("INSERT INTO todos (title, description) VALUES (?, ?) ;", t)
t = ("Todo 2",)
cursor.execute("INSERT INTO todos (title) VALUES (?) ;", t)
t = ("Todo 3", "done")
cursor.execute("INSERT INTO todos (title, status) VALUES (?, ?) ;", t)
t = ("Todo 4",)
cursor.execute("INSERT INTO todos (title) VALUES (?) ;", t)
co.commit()

# TEST DB WITH EXEMPLE
cursor.execute("SELECT * FROM todos")
rows = cursor.fetchall()

for row in rows:
    print(row)

#
cursor.close()
co.close()
