from flask import Flask, render_template, redirect, request
from flask import Blueprint 

from models.genre import Genre
import repositories.genre_repository as genre_repository

genres_blueprint = Blueprint("genres", __name__)

# new
@genres_blueprint.route("/genres/new")
def new_genre():

    return render_template("genres/new.html")

# create
@genres_blueprint.route("/genres", methods = ["POST"])
def create_genre():
    name = request.form["name"]
    new_genre = Genre(name)
    genre_repository.save(new_genre)
    
    return redirect("/mixes/new")