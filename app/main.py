from app.models.taskmodel import Task
from app.services.taskservice import TaskService
from app.database import get_task_by_id

def iniciar():
    service = TaskService()
    
    #loop menu
    while True:
        print_menu()
        
        opcao = input() 

        match opcao:
            #criar
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


            #listar
            case "2":
                tasks = service.list_tasks()

                if not tasks:
                    print("Nenhuma tarefa cadastrada.")
                else:
                    for task in tasks:
                        print(f"#{task.id} | {task.title} | {task.desc} | {task.status}")
            
            
            #editar
            case "3":
                print("Qual tarefa deseja editar?")
                id_edit = int(input("Digite o ID da tarefa que deseja alterar: "))
                nome_edit = input("Digite o novo nome: ")
                desc_edit = input("Digite a nova descrição: ")

                task = service.edit_task(id_edit, nome_edit, desc_edit)
                print(f"Tarefa {task.id} Alterada com sucesso.")
                print(f"Novo titulo: {task.title}, Nova descrição: {task.desc}.")

            
            #deletar
            case "4":
                while True:
                    print("Qual tarefa deseja deletar?: ")
                    
                    try:
                        delete_ID = int(input("digite seu ID: "))
                    except ValueError:
                        print("Digite um ID válido.")
                        continue

                    task = get_task_by_id(delete_ID)
                    
                    if task is None:
                        print("Task inexistente.")
                        continue
                    
                    while True:
                        print(f"Tem certeza que deseja Deletar a tarefa: {task.title}? S/N ")
                        
                        opcao = input().strip().lower()
                        
                        if opcao not in ["s", "n"]:
                            print("Digite uma opção válida")
                            continue
                        if opcao == "s":
                            service.delete_task(task.id)
                            print(f"Tarefa {task.id} - {task.title} deletada com sucesso")
                        
                        break
                    break


            #encerrar
            case "0":
                break

            
            #opção inválida
            case _:
                print("Digite uma opção válida.")
                continue

def print_menu():
    print("LISTA DE TAREFAS")
    print("1 - Criar Tarefa")
    print("2 - Listar Tarefa")
    print("3 - Editar Tarefa")
    print("4 - Deletar Tarefa")
    print("0 - Encerrar Programa")