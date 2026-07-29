import sqlite3
from pathlib import Path

DB_PATH = Path("instance/todo.db")

#db
def get_connection():
    Path("instance").mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    return conn


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            desc TEXT,
            status TEXT DEFAULT 'PENDENTE',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            completed_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


