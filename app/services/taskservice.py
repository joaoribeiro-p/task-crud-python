from app.models.taskmodel import Task
from app.repositories.taskrepository import insert_task, get_all_tasks, update_task, get_task_by_id, db_delete_task, db_complete_update, db_reopen_update

class TaskService:

    
    def create_task(self, title, desc):
        if not title.strip():
            raise ValueError("Titulo obrigatório.")
        
        task = Task(title, desc)

        insert_task(task)
        
        return task
    
    def list_tasks(self):
        return get_all_tasks()
    
    def edit_task(self, task_id, new_title, new_desc):
        if not new_title.strip():
            raise ValueError ("Este campo não pode estar vázio.")
        
        sucesso = update_task(task_id, new_title, new_desc)

        if not sucesso:
            raise ValueError("Tarefa não encontrada")
        
        return get_task_by_id(task_id)
    
    def delete_task(self, task_id):
        db_delete_task(task_id)

    
    
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