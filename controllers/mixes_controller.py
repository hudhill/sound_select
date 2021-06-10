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

# add
