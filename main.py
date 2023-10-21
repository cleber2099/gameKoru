from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, static_url_path='/static', static_folder='static')


db = ["korao@example.com", "koruzim@example.com", "koruzito@gmail.com", "koru@yahoo.com", "superkoru@hotmail.com", "korukoru@outlook.com"]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verificar_email', methods=['POST'])
def verificar_email():
    email = request.form.get('email')

    if email in db:
        mensagem = "E-mail já inscrito."
    else:
        db.append(email)
        mensagem = "Inscrito com sucesso!"

    return render_template('index.html', mensagem=mensagem)


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


if __name__ == '__main__':
    app.run()

    #alt