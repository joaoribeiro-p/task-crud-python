from datetime import datetime

class Task:

    STATUS_PENDENTE = "PENDENTE"
    STATUS_CONCLUIDA = "CONCLUIDA"

    def __init__(
        self,
        title,
        desc,
        status=None,
        created_at=None,
        completed_at=None,
        task_id=None
    ):

        self.title = title
        self.desc = desc

        self.status = status or self.STATUS_PENDENTE

        self.created_at = created_at or datetime.now()

        self.completed_at = completed_at

        self.id = task_id

    def complete_task(self):
        if self.status == self.STATUS_CONCLUIDA:
            raise ValueError("Tarefa ja concluida.")
        
        self.status = self.STATUS_CONCLUIDA
        self.completed_at = datetime.now()
    
    def reopen(self):
        if self.status == self.STATUS_PENDENTE:
            raise ValueError("Tarefa em andamento.")
        
        self.status = self.STATUS_PENDENTE
        self.completed_at = None