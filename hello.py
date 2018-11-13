from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World in Flask</h1>'

@app.route('/animals/<name>')
def przywitajZwierza(name):
    return f'<h1>Witaj {name}</h1>'