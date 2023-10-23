from main import app
from flask import render_template
from flask import request
from data  import db

@app.route('/secemail', methods=['POST'])
def secemail():
    email = request.form.get('email')

    if email in db:
        mensagem = "E-mail já inscrito."
    else:
        db.append(email)
        mensagem = "Inscrito com sucesso!"

    return render_template('index.html', mensagem=mensagem)