from app.models.taskmodel import Task
from app.repositories.taskrepository import Repository as repository


class TaskService:

# =========================
# CREATE
# =========================
    def create_task(self, title, desc):
        if not title.strip():
            raise ValueError("Titulo obrigatório.")
        
        task = Task(title, desc)

        repository.insert_task(task)
        
        return task
    

# =========================
# READ
# =========================
    def list_tasks(self):
        return repository.get_all_tasks()
    
    def list_tasks_by_status(self, status, limit=None, page=None, per_page=None):
        return repository.get_tasks_by_status(
            status=status,
            limit=limit,
            page=page,
            per_page=per_page
        )
    
    def count_tasks_by_status(self, status):
        return repository.count_tasks_by_status(status)
# =========================
# UPDATE
# =========================

    def edit_task(self, task_id, new_title, new_desc):

        if not new_title.strip():
            raise ValueError("Este campo não pode estar vazio.")

        task = repository.get_task_by_id(task_id)

        if task is None:
            raise ValueError("Tarefa não encontrada.")

        if task.status == "CONCLUIDA":
            raise ValueError(
                "Uma tarefa concluída não pode ser editada. Reabra antes de editar."
            )

        sucesso = repository.update_task(task_id, new_title, new_desc)

        if not sucesso:
            raise ValueError("Erro ao atualizar tarefa.")

        return repository.get_task_by_id(task_id)
       
    
    def complete_task(self, task_id):
        
        task = repository.get_task_by_id(task_id)

        if task is None:
            raise ValueError("Task inexistente.")
        
        task.complete()
        
        repository.db_complete_update(task) 
        return repository.get_task_by_id(task.id)

    
    def reopen_task(self, task_id):

        task = repository.get_task_by_id(task_id)

        if task is None:
            raise ValueError("Task inexistente.")
        
        task.reopen()
        repository.db_reopen_update(task)
        return repository.get_task_by_id(task.id)
    

# =========================
# DELETE
# =========================
    def hard_delete(self, task_id):
        task = repository.get_all_tasks_including_deleted(task_id)

        if task is None:
            raise ValueError("Tarefa não encontrada.")
        
        return repository.hard_delete_task(task_id)


    def soft_delete(self, task_id):
        task = repository.get_task_by_id(task_id)

        if task is None:
            raise ValueError("Tarefa não encontrada.")

        return repository.soft_delete_task(task_id)
    
    def restore_task(self, task_id):
        task = repository.get_all_tasks_including_deleted(task_id)

        if task is None:
            raise ValueError("Tarefa não encontrada.")

        if task.status != Task.EXCLUIDA:
            raise ValueError("A tarefa não está excluída.")

        return repository.restore_task(task_id)