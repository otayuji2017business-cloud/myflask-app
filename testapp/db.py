#SQLAlchemy 採用により使わなくなった


import sqlite3

DB_NAME = "data.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()



def save_user(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name) VALUES (?)", (name,))

    conn.commit()
    conn.close()


def get_users():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM users")
    rows = cur.fetchall()

    conn.close()
    return rows

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )

    conn.commit()
    conn.close()


def update_user(user_id, name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET name = ? WHERE id = ?",
        (name, user_id)
    )

    conn.commit()
    conn.close()


def get_user(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name FROM users WHERE id = ?",
        (user_id,)
    )

    user = cur.fetchone()

    conn.close()
    return user