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
@djs_blueprint.route("/djs")

# add