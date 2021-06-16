from flask import Flask, render_template, redirect, request
from flask import Blueprint 

from models.genre import Genre
import repositories.genre_repository as genre_repository
import repositories.mix_repository as mix_repository

genres_blueprint = Blueprint("genres", __name__)

# new
@genres_blueprint.route("/genres/new")
def new_genre():

    return render_template("genres/new.html")

# create
@genres_blueprint.route("/genres", methods = ["POST"])
def create_genre():
    name = request.form["name"]
    color = request.form["color"]
    new_genre = Genre(name, color)
    genre_repository.save(new_genre)
    
    return redirect("/mixes/new")  # only in use when creating new mix, so redirects you to new mix form

# show
@genres_blueprint.route("/genres/<id>")
def show_genre(id):
    genre = genre_repository.select(id)
    mixes = mix_repository.select_by_genre(id)

    return render_template("genres/show.html", genre=genre, mixes=mixes)