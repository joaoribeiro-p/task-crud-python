from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/editar")
def edit():
    return render_template("edit.html")
