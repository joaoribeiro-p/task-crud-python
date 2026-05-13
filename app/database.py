import sqlite3
from pathlib import Path
from app.models.taskmodel import Task

DB_PATH = Path("instance/todo.db")


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

#inserir task no db
def insert_task(task):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (title, desc, status, created_at, completed_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        task.title,
        task.desc,
        task.status,
        task.created_at,
        task.completed_at
    ))

    conn.commit()
    
    task.id = cursor.lastrowid
    
    conn.close()

#listar tasks
def get_all_tasks():        
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, desc, status, created_at, completed_at
        FROM tasks
    """)
    rows = cursor.fetchall()
    conn.close()
    tasks = []
    for row in rows:
        task = Task(
            title=row[1],
            desc=row[2],
            status=row[3],
            created_at=row[4],
            completed_at=row[5],
            task_id=row[0]
        )
        tasks.append(task)
    return tasks

