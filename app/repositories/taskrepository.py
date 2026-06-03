from app.database import get_connection
from app.models.taskmodel import Task


# =========================
# AUXILIAR
# =========================
def row_to_task(row):
    return Task(
        title=row[1],
        desc=row[2],
        status=row[3],
        created_at=row[4],
        completed_at=row[5],
        task_id=row[0]
    )

class Repository:
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
            WHERE status != ?
            ORDER BY id DESC
        """, ("EXCLUIDA",))

        rows = cursor.fetchall()
        conn.close()

        return [row_to_task(row) for row in rows]

    def get_task_by_id(task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, title, desc, status, created_at, completed_at
            FROM tasks
            WHERE id = ?
            AND status != ?
        """, (task_id, "EXCLUIDA"))

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None

        return row_to_task(row)

    def get_tasks_by_status(status, limit=None, page=None, per_page=None):
        conn = get_connection()
        cursor = conn.cursor()

        order_by = "created_at DESC"

        if status == "CONCLUIDA":
            order_by = "completed_at DESC"

        query = f"""
            SELECT id, title, desc, status, created_at, completed_at
            FROM tasks
            WHERE status = ?
            ORDER BY {order_by}
        """

        params = [status]

        if page is not None and per_page is not None:
            offset = (page - 1) * per_page
            query += " LIMIT ? OFFSET ?"
            params.extend([per_page, offset])
        
        elif limit is not None:
            query += " LIMIT ?"
            params.append(limit)


        cursor.execute(query, params)

        rows = cursor.fetchall()
        conn.close()

        return [row_to_task(row) for row in rows]
    
    def count_tasks_by_status(status):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM tasks
            WHERE status = ?
        """, (status,))

        total = cursor.fetchone()[0]
        conn.close()

        return total

    def get_all_tasks_including_deleted(task_id):        
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

        return row_to_task(row)

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
    def hard_delete_task(task_id):
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

    def soft_delete_task(task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tasks
            SET status = ?
            WHERE id = ?
        """, ("EXCLUIDA", task_id))

        conn.commit()
        affected_rows = cursor.rowcount
        conn.close()

        return affected_rows > 0


    