from app.services.taskservice import TaskService
from app.repositories.taskrepository import get_task_by_id

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
                while True:
                    menu_edit()
                    opcaoEdit = input()

                    match opcaoEdit:
                        case "1":
                            while True:

                                try:

                                    try:
                                        id_edit = int(input("Digite o ID da tarefa: "))
                                    except ValueError:
                                        print("Digite um número válido.")
                                        continue
                                    
                                    task_exist = get_task_by_id(id_edit)
                                    if task_exist is None:
                                        print("Nenhuma tarefa encontrada.")
                                        continue

                                    nome_edit = input("Novo nome: ").strip()
                                    desc_edit = input("Nova descrição: ").strip()

                                    task = service.edit_task(id_edit, nome_edit, desc_edit)

                                    print(f"Tarefa #{task.id} alterada com sucesso.")

                                    break

                                except ValueError as error:
                                    print(f"Erro: {error}")
                                                 
                        case "2":
                            print("Qual tarefa deseja COMPLETAR?")
                            try:                             
                                id_complete = int(input())
                            except ValueError:
                                print("Digite um ID válido")
                                continue

                            task = service.complete_task(id_complete)
                            
                            print(f"Tarefa {task.id} - {task.title} está completa.")

                        case "3":
                            print("Qual tarefa deseja REABRIR?")
                            try:                             
                                id_reopen = int(input())
                            except ValueError:
                                print("Digite um ID válido")
                                continue

                            task = service.reopen_task(id_reopen)
                            
                            print(f"Tarefa {task.id} - {task.title} está reaberta.")

                        case "0":
                            break

                        case _:
                            print("Digite uma opção válida")
                            continue

            
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
    print("3 - Editar, Concluir ou Reabrir tarefa")
    print("4 - Deletar Tarefa")
    print("0 - Encerrar Programa")

def menu_edit():
    print("-- MENU EDIÇÃO --")
    print("1 - Editar nome e descrição")
    print("2 - Concluir tarefa")
    print("3 - Reabrir tarefa")
    print("0 - Voltar")