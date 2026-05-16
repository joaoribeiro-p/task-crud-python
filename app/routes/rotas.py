from flask import Blueprint, render_template, request, redirect, url_for
from app.services.taskservice import TaskService
from app.database import get_task_by_id


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
