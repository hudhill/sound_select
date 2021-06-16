from flask import Flask, render_template, redirect
from flask import Blueprint 

import repositories.mix_repository as mix_repository

mysource_blueprint = Blueprint("mysource", __name__)

# index
@mysource_blueprint.route("/mysource")
def mymixes():
    mixes = mix_repository.select_by_mysource()

    return render_template("mysource/index.html", mixes=mixes)

# update mysource to True
@mysource_blueprint.route("/mysource/<id>", methods = ['POST'])
def mysource_true(id):
    mix = mix_repository.select(id)
    mix_repository.mysource_true(mix)

    return redirect("/mysource")

#update mysource to False
@mysource_blueprint.route("/mysource/<id>/delete", methods=['POST'])
def mysource_false(id):
    mix = mix_repository.select(id)
    mix_repository.mysource_false(mix)

    return redirect("/mysource")