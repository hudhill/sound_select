from flask import Flask, render_template

# import all controllers
from controllers.mixes_controller import mixes_blueprint
from controllers.djs_controller import djs_blueprint
from controllers.genres_controller import genres_blueprint

app = Flask(__name__)

# register all blueprints
app.register_blueprint(mixes_blueprint)
app.register_blueprint(djs_blueprint)
app.register_blueprint(genres_blueprint)

# Home Page:
@app.route('/') 
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)