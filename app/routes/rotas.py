from flask import Blueprint, render_template, request, redirect, url_for
from app.services.taskservice import TaskService
from app.repositories.taskrepository import get_task_by_id


main = Blueprint("main", __name__)
service = TaskService()

@main.route("/")
def index():
    tasks = service.list_tasks()
    
    return render_template("index.html", tasks=tasks)

@main.route("/editar/<int:task_id>")
def edit(task_id):
    
    task = get_task_by_id(task_id)

    return render_template("edit.html", task=task)

@main.route("/criar", methods=["POST"])
def criar_tarefa():

    title = request.form["title"]
    
    desc = request.form["desc"] 

    task = service.create_task(title, desc)

@main.route("/complete/<int:task_id>", methods=["POST"])
def complete(task_id):
    service.complete_task(task_id)
    return redirect(url_for("main.index"))

@main.route("/reopen/<int:task_id>", methods=["POST"])
def reopen(task_id):
    service.reopen_task(task_id)
    return redirect(url_for("main.index"))