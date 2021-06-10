from flask import Flask, render_template, redirect, request
from flask import Blueprint 

from models.mix import Mix
from models.dj import Dj
import repositories.mix_repository as mix_repository
import repositories.dj_repository as dj_repository

mixes_blueprint = Blueprint("mixes", __name__)

# index
@mixes_blueprint.route("/mixes")
def mixes():
    mixes = mix_repository.select_all()

    return render_template("mixes/index.html", mixes=mixes)

# new
@mixes_blueprint.route("/mixes/new")
def new_mix():
    djs = dj_repository.select_all()

    return render_template("mixes/new.html", djs=djs)

# create
@mixes_blueprint.route("/mixes", methods = ["POST"])
def create_mix():
    title = request.form["title"]
    description = request.form["description"]
    dj_id = request.form["dj_id"]
    dj = dj_repository.select(dj_id)
    new_mix = Mix(title, description, dj)
    mix_repository.save(new_mix)

    return redirect("/mixes")

# show
@mixes_blueprint.route("/mixes/<id>")
def show_mix(id):
    mix = mix_repository.select(id)

    return render_template("mixes/show.html", mix=mix)

# edit
@mixes_blueprint.route("/mixes/<id>/edit")
def edit_mix(id):
    mix = mix_repository.select(id)
    djs = dj_repository.select_all()

    return render_template("mixes/edit.html", mix=mix, djs=djs)

# update
@mixes_blueprint.route("/mixes/<id>", methods = ["POST"])
def update_mix(id):
    title = request.form["title"]
    description = request.form["description"]
    dj_id = request.form["dj_id"]
    dj = dj_repository.select(dj_id)
    updated_mix = Mix(title, description, dj, id)
    mix_repository.update(updated_mix)

    return redirect("/mixes")

# delete
@mixes_blueprint.route("/mixes/<id>/delete", methods = ["POST"])
def delete_mix(id):
    mix_repository.delete(id)
    
    return redirect("/mixes")