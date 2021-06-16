from flask import Flask, render_template, redirect, request
from flask import Blueprint 

from models.dj import Dj
import repositories.mix_repository as mix_repository
import repositories.dj_repository as dj_repository

djs_blueprint = Blueprint("djs", __name__)

# index
@djs_blueprint.route("/djs")
def djs():
    djs = dj_repository.select_all()

    return render_template("djs/index.html", djs=djs)

# new
@djs_blueprint.route("/djs/new")
def new_dj():

    return render_template("djs/new.html")

# create
@djs_blueprint.route("/djs", methods = ["POST"])
def create_dj():
    name = request.form["name"]
    img = request.form["img"]
    new_dj = Dj(name, img)
    dj_repository.save(new_dj)
    
    return redirect("/djs")

# show
@djs_blueprint.route("/djs/<id>")
def show_dj(id):
    dj = dj_repository.select(id)
    mixes = mix_repository.select_by_dj(id)

    return render_template("djs/show.html", dj=dj, mixes=mixes)

# edit
@djs_blueprint.route("/djs/<id>/edit")
def edit_dj(id):
    dj = dj_repository.select(id)

    return render_template("djs/edit.html", dj=dj)

# update
@djs_blueprint.route("/djs/<id>", methods = ["POST"])
def update_dj(id):
    name = request.form["name"]
    img = request.form["img"]
    updated_dj = Dj(name, img, id)
    dj_repository.update(updated_dj)

    return redirect("/djs")

# delete
@djs_blueprint.route("/djs/<id>/delete", methods = ["POST"])
def delete_dj(id):
    dj_repository.delete(id)

    return redirect("/djs")