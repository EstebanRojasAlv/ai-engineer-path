import sqlite3

MATERIALS = [
    ("cement", 32000),
    ("sand", 85000),
    ("steel", 140000),
    ("gravel", 60000),
]


UPSERT_SQL = (
    "INSERT INTO materials (name, price) VALUES (?, ?) "
    "ON CONFLICT(name) DO UPDATE SET price = excluded.price"
    )

connection = sqlite3.connect("practice.db")

try:

    connection.execute("""
                    CREATE TABLE IF NOT EXISTS materials (
                    id INTEGER PRIMARY KEY,
                    name TEXT UNIQUE NOT NULL,
                    price INTEGER NOT NULL
                    )
    """)

    connection.executemany(UPSERT_SQL, MATERIALS)
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

finally:
    connection.close()
    