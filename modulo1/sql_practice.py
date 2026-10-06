import sqlite3

connection = sqlite3.connect("practice.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
    )
""")

connection.execute(
    "INSERT INTO materials (name, price) VALUES (?, ?)",
    ("cement", 32000),
)
connection.execute(
    "INSERT INTO materials (name, price) VALUES (?, ?)",
    ("sand", 85000),
)
connection.execute(
    "INSERT INTO materials (name, price) VALUES (?, ?)",
    ("steel", 120000)
)
connection.commit()

rows = connection.execute(
    "SELECT name, price FROM materials ORDER BY price DESC"
).fetchall()

for name, price in rows:
    print(f"{name}: {price}")

expensive = connection.execute(
    "SELECT name, price FROM materials WHERE price > ? ORDER BY price DESC",
    (50000,),
).fetchall()

for name, price in expensive:
    print(f"Expensive material {name}: {price}")


connection.close()
    