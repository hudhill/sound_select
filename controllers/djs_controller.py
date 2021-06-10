from flask import Flask, render_template, redirect, request
from flask import Blueprint 

from models.mix import Mix
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
    bio = request.form["bio"]
    new_dj = Dj(name, bio)
    dj_repository.save(new_dj)
    
    return redirect("/djs")


# New dj option for new mix:
# @djs_blueprint.route("/djs/new_option")
# def new_dj_option():

#     return render_template("djs/new_option.html")

# Return to new mix form:
# @djs_blueprint.route("/djs/option", methods = ["POST"])
# def create_new_option():
#     name = request.form["name"]
#     new_dj = Dj(name)
#     dj_repository.save(new_dj)

#     return redirect("/mixes/new")


# show
@djs_blueprint.route("/djs/<id>")
def show_dj(id):
    dj = dj_repository.select(id)

    return render_template("djs/show.html", dj=dj)

# edit
@djs_blueprint.route("/djs/<id>/edit")
def edit_dj(id):
    dj = dj_repository.select(id)

    return render_template("djs/edit.html", dj=dj)

# update
@djs_blueprint.route("/djs/<id>", methods = ["POST"])
def update_dj(id):
    name = request.form["name"]
    bio = request.form["bio"]
    updated_dj = Dj(name, bio, id)
    dj_repository.update(updated_dj)

    return redirect("/djs")

# delete
@djs_blueprint.route("/djs/<id>/delete", methods = ["POST"])
def delete_dj(id):
    dj_repository.delete(id)

    return redirect("/djs")