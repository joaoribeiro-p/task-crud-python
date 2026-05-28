from app.database import get_connection
from app.models.taskmodel import Task

# =========================
# CREATE
# =========================
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


# =========================
# READ
# =========================
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

def get_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, desc, status, created_at, completed_at
        FROM tasks
        WHERE id = ?
    """, (task_id,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    task = Task(
        title=row[1],
        desc=row[2],
        status=row[3],
        created_at=row[4],
        completed_at=row[5],
        task_id=row[0]
    )

    return task

def get_completed_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tasks
        WHERE status = 'CONCLUIDA'
        ORDER BY completed_at DESC
        LIMIT 5
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

def get_completed_tasks_paginated(limit, offset):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, desc, status, created_at, completed_at
        FROM tasks
        WHERE status = ?
        ORDER BY completed_at DESC
        LIMIT ? OFFSET ?
    """, ("CONCLUIDA", limit, offset))

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

def count_completed_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE status = ?
    """, ("CONCLUIDA",))

    total = cursor.fetchone()[0]
    conn.close()

    return total 

# =========================
# UPDATE
# =========================
def update_task(task_id, new_title, new_desc):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET title = ?, desc = ?
        WHERE id = ?
    """, (
        new_title,
        new_desc,
        task_id
    ))

    conn.commit()

    updated_rows = cursor.rowcount

    conn.close()

    return updated_rows > 0 

def db_complete_update(task):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = ?, completed_at = ?
        WHERE id = ?
    """, (
        task.status,
        task.completed_at,
        task.id
    ))

    conn.commit()
    conn.close()

def db_reopen_update(task):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = ?, completed_at = ?
        WHERE id = ?
    """, (
        task.status,
        task.completed_at,
        task.id
    ))

    conn.commit()
    conn.close()



# =========================
# DELETE
# =========================
def db_delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (
        task_id,
    ))

    conn.commit()

    updated_rows = cursor.rowcount

    conn.close()
    return updated_rows > 0