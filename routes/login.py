from main import app
from flask import render_template
from flask import request
from data  import db

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'koru' and password == 'koru':
            return render_template('adm.html', emails=db)
        else:
            mensagem = 'User não autorizado'
            return render_template('login.html', mensagem=mensagem)

    return render_template('login.html')