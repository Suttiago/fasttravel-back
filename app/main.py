from flask import Blueprint, render_template, request, redirect, url_for, app,Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from controllers.UserController import user_bp
from controllers.DestinoController import destio_bp
from controllers.PessoaController import pessoa_bp
from controllers.HotelsController import hotel_bp
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__, template_folder="templates")
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
jwt = JWTManager(app)

app.secret_key = os.getenv('SECRET_KEY')
app.register_blueprint(destio_bp)
app.register_blueprint(user_bp, url_prefix = '/Usuario')
app.register_blueprint(pessoa_bp,url_prefix='/Dependentes')
app.register_blueprint(hotel_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)




