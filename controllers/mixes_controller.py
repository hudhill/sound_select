from flask import Flask, render_template, redirect, request
from flask import Blueprint 

from models.mix import Mix
import repositories.mix_repository as mix_repository
import repositories.dj_repository as dj_repository
import repositories.genre_repository as genre_repository

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
    genres = genre_repository.select_all()

    return render_template("mixes/new.html", djs=djs, genres=genres)

# create
@mixes_blueprint.route("/mixes", methods = ["POST"])
def create_mix():
    title = request.form["title"]
    description = request.form["description"]
    mix_img = request.form["mix_img"]
    tracklist_img = request.form["tracklist_img"]
    genre_tags = request.form["genre_tags"]
    audio_link = request.form["audio_link"]
    mysource = request.form["mysource"]
    genre_id = request.form["genre_id"]
    genre = genre_repository.select(genre_id)
    dj_id = request.form["dj_id"]
    dj = dj_repository.select(dj_id)
    new_mix = Mix(title, description, mix_img, tracklist_img, genre_tags, audio_link, genre, dj, mysource)
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
    genres = genre_repository.select_all()

    return render_template("mixes/edit.html", mix=mix, djs=djs, genres=genres)

# update
@mixes_blueprint.route("/mixes/<id>", methods = ["POST"])
def update_mix(id):
    title = request.form["title"]
    description = request.form["description"]
    mix_img = request.form["mix_img"]
    tracklist_img = request.form["tracklist_img"]
    genre_tags = request.form["genre_tags"]
    audio_link = request.form["audio_link"]
    mysource = request.form["mysource"]
    genre_id = request.form["genre_id"]
    genre = genre_repository.select(genre_id)
    dj_id = request.form["dj_id"]
    dj = dj_repository.select(dj_id)
    updated_mix = Mix(title, description, mix_img, tracklist_img, genre_tags, audio_link, genre, dj, mysource, id)
    mix_repository.update(updated_mix)

    return redirect("/mixes")

# delete
@mixes_blueprint.route("/mixes/<id>/delete", methods = ["POST"])
def delete_mix(id):
    mix_repository.delete(id)
    
    return redirect("/mixes")