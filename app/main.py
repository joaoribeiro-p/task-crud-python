from app.models.taskmodel import Task
from app.services.taskservice import TaskService

def iniciar():
    service = TaskService()
    
    while True:
        print("LISTA DE TAREFAS")
        print("1 - Criar Tarefa")
        print("2 - Listar Tarefa")
        print("0 - Encerrar Programa")
        opcao = input()

        match opcao:

            case "1":
                print("Digite a tarefa que quer adicionar a lista: ")
                nometarefa = input("> ")
                print("Agora sua descrição")
                desctarefa = input("> ")

                try:
                    nova_tarefa = service.create_task(nometarefa, desctarefa)
                    print(f"Tarefa #{nova_tarefa.id}: {nova_tarefa.title}, adicionada.")
                except ValueError as erro:
                    print(f"Erro: {erro}")

            case "2":
                tasks = service.list_tasks()

                if not tasks:
                    print("Nenhuma tarefa cadastrada.")
                else:
                    for task in tasks:
                        print(f"#{task.id} | {task.title} | {task.desc} | {task.status}")
            
            case "0":
                break

            case _:
                return("Digite uma opção válida.")