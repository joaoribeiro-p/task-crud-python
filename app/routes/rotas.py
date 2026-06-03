from flask import Blueprint, render_template, request, redirect, url_for
from app.services.taskservice import TaskService
from app.models.taskmodel import Task


main = Blueprint("main", __name__)
service = TaskService()

@main.route("/")
def index():
    pending_tasks = service.list_tasks_by_status("PENDENTE", limit=5)
    completed_tasks = service.list_tasks_by_status("CONCLUIDA", limit=5)

    return render_template(
        "index.html",
        pending_tasks=pending_tasks,
        completed_tasks=completed_tasks
    )

@main.route("/editar/<int:task_id>", methods=["POST"])
def edit(task_id):

    title = request.form["title"]
    desc = request.form["desc"]

    service.edit_task(task_id, title, desc)
    return redirect(url_for("main.index"))

@main.route("/criar", methods=["POST"])
def criar_tarefa():

    title = request.form["title"]
    
    desc = request.form["desc"] 

    service.create_task(title, desc)
    
    return redirect(url_for("main.index"))


@main.route("/complete/<int:task_id>", methods=["POST"])
def complete(task_id):
    service.complete_task(task_id)
    return redirect(url_for("main.index"))

@main.route("/reopen/<int:task_id>", methods=["POST"])
def reopen(task_id):
    service.reopen_task(task_id)
    return redirect(url_for("main.index"))




@main.route("/concluidas")
def concluidas():
    page = request.args.get("page", 1, type=int)
    per_page = 5

    tasks = service.list_tasks_by_status(
        status=Task.CONCLUIDA,
        page=page,
        per_page=per_page
    )

    total_tasks = service.count_tasks_by_status(Task.CONCLUIDA)
    total_pages = (total_tasks + per_page - 1) // per_page

    return render_template(
        "concluidas.html",
        tasks=tasks,
        page=page,
        total_pages=total_pages
    )

@main.route("/excluidas")
def excluidas():
    page = request.args.get("page", 1, type=int)
    per_page = 5

    tasks = service.list_tasks_by_status(
        status=Task.EXCLUIDA,
        page=page,
        per_page=per_page
    )

    total_tasks = service.count_tasks_by_status(Task.EXCLUIDA)
    total_pages = (total_tasks + per_page - 1) // per_page

    return render_template(
        "excluidas.html",
        tasks=tasks,
        page=page,
        total_pages=total_pages
    )

@main.route("/restaurar/<int:task_id>", methods=["POST"])
def restore(task_id):
    service.restore_task(task_id)
    return redirect(url_for("main.excluidas"))

@main.route("/hard_delete/<int:task_id>", methods=["POST"])
def hard_delete(task_id):
    service.hard_delete(task_id)
    return redirect (url_for("main.excluidas"))

@main.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    service.soft_delete(task_id)
    return redirect(url_for("main.index"))
