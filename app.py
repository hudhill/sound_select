from flask import Flask, render_template

# import all controllers

app = Flask(__name__)

# register all blueprints

# Home Page:
@app.route('/') 
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)