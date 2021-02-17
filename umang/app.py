from flask import Flask, render_template
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from os import path
from flask import CORS

from user import UserRegister

template_dir = path.abspath("../Demo")
app = Flask(__name__, template_folder=template_dir)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'afour'
api = Api(app)
CORS(app)

api.add_resource(UserRegister, '/register')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/landing')
def landing():
    return render_template('landing.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)  # important to mention debug=True

app = Flask(__name__)
