from main import app
from flask import render_template
from flask import request

usuarios = {}


@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuarios[email] = {
        'nome' : nome,
        'email' : email,
        'senha' : senha
    }
    return render_template('cadastro.html')