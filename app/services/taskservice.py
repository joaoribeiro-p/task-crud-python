from datetime import datetime
from app.models.taskmodel import Task
from app.database import insert_task, get_all_tasks

class TaskService:

    
    def create_task(self, title, desc):
        if not title.strip():
            raise ValueError("Titulo obrigatório.")
        
        task = Task(title, desc)

        insert_task(task)
        
        return task
    
    def list_tasks(self):
        return get_all_tasks()