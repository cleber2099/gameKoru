from flask import Flask
from routes.verificaemail import secemail
from routes.cadastro import cadastro
from routes.login  import login
from routes.home import home

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

app.register_blueprint(secemail)
app.register_blueprint(cadastro)
app.register_blueprint(login)
app.register_blueprint(home)


if __name__ == '__main__':
    app.run()
