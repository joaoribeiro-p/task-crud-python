from app.models.taskmodel import Task
from app.repositories.taskrepository import insert_task, get_all_tasks, update_task, get_task_by_id, db_delete_task, db_complete_update, db_reopen_update
from app.repositories.taskrepository import get_completed_tasks, get_completed_tasks_paginated, count_completed_tasks
import math

class TaskService:

# =========================
# CREATE
# =========================
    def create_task(self, title, desc):
        if not title.strip():
            raise ValueError("Titulo obrigatório.")
        
        task = Task(title, desc)

        insert_task(task)
        
        return task
    

# =========================
# READ
# =========================
    def list_tasks(self):
        return get_all_tasks()
    
    def list_completed_tasks(self):
        return get_completed_tasks()
    
    def list_completed_tasks_paginated(self, page=1, per_page=5):
        offset = (page - 1) * per_page

        tasks = get_completed_tasks_paginated(per_page, offset)
        total_tasks = count_completed_tasks()

        total_pages = math.ceil(total_tasks / per_page)

        return tasks, total_pages
    
# =========================
# UPDATE
# =========================

    def edit_task(self, task_id, new_title, new_desc):

        if not new_title.strip():
            raise ValueError("Este campo não pode estar vazio.")

        task = get_task_by_id(task_id)

        if task is None:
            raise ValueError("Tarefa não encontrada.")

        if task.status == "CONCLUIDA":
            raise ValueError(
                "Uma tarefa concluída não pode ser editada. Reabra antes de editar."
            )

        sucesso = update_task(task_id, new_title, new_desc)

        if not sucesso:
            raise ValueError("Erro ao atualizar tarefa.")

        return get_task_by_id(task_id)
       
    
    def complete_task(self, task_id):
        
        task = get_task_by_id(task_id)

        if task is None:
            raise ValueError("Task inexistente.")
        
        task.complete()
        
        db_complete_update(task) 
        return get_task_by_id(task.id)

    
    def reopen_task(self, task_id):

        task = get_task_by_id(task_id)

        if task is None:
            raise ValueError("Task inexistente.")
        
        task.reopen()
        db_reopen_update(task)
        return get_task_by_id(task.id)


# =========================
# DELETE
# =========================
    def delete_task(self, task_id):
        db_delete_task(task_id)