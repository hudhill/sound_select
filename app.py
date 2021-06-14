from flask import Flask, render_template

# import all controllers
from controllers.mixes_controller import mixes_blueprint
from controllers.djs_controller import djs_blueprint
from controllers.genres_controller import genres_blueprint
from controllers.mysource_controller import mysource_blueprint

import repositories.genre_repository as genre_repository

app = Flask(__name__)

# register all blueprints
app.register_blueprint(mixes_blueprint)
app.register_blueprint(djs_blueprint)
app.register_blueprint(genres_blueprint)
app.register_blueprint(mysource_blueprint)

# Home Page:
@app.route('/') 
def home():
    genres = genre_repository.select_all()
    return render_template('home.html', genres=genres)

if __name__ == '__main__':
    app.run(debug=True)