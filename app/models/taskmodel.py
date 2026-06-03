from datetime import datetime

class Task:

    PENDENTE = "PENDENTE"
    CONCLUIDA = "CONCLUIDA"
    EXCLUIDA = "EXCLUIDA"



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

        self.status = status or self.PENDENTE

        self.created_at = created_at or datetime.now()

        self.completed_at = completed_at

        self.id = task_id

    def complete(self):
        if self.status == self.CONCLUIDA:
            raise ValueError("Tarefa ja concluida.")
        
        self.status = self.CONCLUIDA
        self.completed_at = datetime.now()
    
    def reopen(self):
        if self.status == self.PENDENTE:
            raise ValueError("Tarefa em andamento.")
        
        self.status = self.PENDENTE
        self.completed_at = None

    def delete(self):
        if self.status == self.EXCLUIDA:
            raise ValueError("Tarefa já excluida.")
        
        self.status = self.EXCLUIDA

    def restore(self):
        self.status = self.PENDENTE