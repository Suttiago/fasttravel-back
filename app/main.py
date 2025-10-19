from flask import Blueprint, render_template, request, redirect, url_for, app,Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from controllers.UserController import user_bp
from controllers.DestinoController import destio_bp
from controllers.PessoaController import pessoa_bp
from controllers.HotelsController import hotel_bp
from controllers.CidadeController import cidade_bp
from controllers.PassagensController import passagem_bp
from controllers.OrcamentoController import orcamento_bp
from controllers.ContasPagarController import pagar_bp
from controllers.PlanoPagamentoController import plano_bp
from controllers.RelatorioController import relatorio_bp
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__, template_folder="templates")
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
jwt = JWTManager(app)

app.secret_key = os.getenv('SECRET_KEY')
app.register_blueprint(destio_bp, url_prefix='/Destinos')
app.register_blueprint(user_bp, url_prefix = '/Usuario')
app.register_blueprint(pessoa_bp,url_prefix='/Dependentes')
app.register_blueprint(cidade_bp, url_prefix='/Cidades')
app.register_blueprint(hotel_bp)
app.register_blueprint(passagem_bp)
app.register_blueprint(orcamento_bp, url_prefix='/Orcamento')
app.register_blueprint(pagar_bp, url_prefix ='/Contas')
app.register_blueprint(plano_bp, url_prefix ='/Plano')
app.register_blueprint(relatorio_bp, url_prefix ='/Relatorio')
app


if __name__ == '__main__':
    app.run(debug=True, port=5001)  




