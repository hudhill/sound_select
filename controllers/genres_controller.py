from flask import Flask, render_template, redirect, request
from flask import Blueprint 

from models.genre import Genre
import repositories.genre_repository as genre_repository
import repositories.mix_repository as mix_repository

genres_blueprint = Blueprint("genres", __name__)

# New
@genres_blueprint.route("/genres/new")
def new_genre():

    return render_template("genres/new.html")

# Create
@genres_blueprint.route("/genres", methods = ["POST"])
def create_genre():
    name = request.form["name"]
    color = request.form["color"]
    new_genre = Genre(name, color)

    genres = genre_repository.select_all()
    genre_names = []
    for genre in genres:
        genre_names.append(genre.name)
        if new_genre.name == genre.name:
            new_genre.id = genre.id

    if new_genre.name not in genre_names:
        genre_repository.save(new_genre)
    
    return redirect("/mixes/new")  # only in use when creating new mix, so redirects you to new mix form

# Show
@genres_blueprint.route("/genres/<id>")
def show_genre(id):
    genre = genre_repository.select(id)
    mixes = mix_repository.select_by_genre(id)

    return render_template("genres/show.html", genre=genre, mixes=mixes)