from flask import Blueprint, render_template, request, redirect, url_for
from app.services.taskservice import TaskService
from app.repositories.taskrepository import get_task_by_id


main = Blueprint("main", __name__)
service = TaskService()

@main.route("/")
def index():

    tasks = service.list_tasks()

    pending_tasks = [
        task for task in tasks
        if task.status == "PENDENTE"
    ]

    completed_tasks = service.list_completed_tasks()

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

@main.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    service.delete_task(task_id)
    return redirect(url_for("main.index"))



#@main.route("/concluidas")
#def completed_tasks():
    tasks = service.list_completed_tasks()
    return render_template("concluidas.html", tasks=tasks)

@main.route("/concluidas")
def concluidas():
    page = request.args.get("page", 1, type=int)
    per_page = 5

    tasks, total_pages = service.list_completed_tasks_paginated(page, per_page)

    return render_template(
        "concluidas.html",
        tasks=tasks,
        page=page,
        total_pages=total_pages
    )