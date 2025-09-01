from flask import Blueprint, render_template, request, redirect, url_for, app,Flask
from controllers.UserController import user_bp
from controllers.DestinoController import destio_bp
from controllers.PessoaController import pessoa_bp
from controllers.HotelsController import hotel_bp
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__, template_folder="templates")
app.secret_key = os.getenv('SECRET_KEY')
app.register_blueprint(user_bp)
app.register_blueprint(destio_bp)
app.register_blueprint(pessoa_bp)
app.register_blueprint(hotel_bp)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/CadastroUsuario', methods=['GET'])
def users():
    return render_template('cadastro.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)




