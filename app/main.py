from flask import Blueprint, render_template, request, redirect, url_for, app,Flask
from controllers.UserController import user_bp
from controllers.DepedentaController import dependente_bp
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__, template_folder="templates")
app.secret_key = os.getenv('SECRET_KEY')
app.register_blueprint(user_bp)

@app.route('/usuarios', methods=['GET'])
def users():
    return render_template('cadastro.html')


app.register_blueprint(dependente_bp)
@app.route('/CadastroDependentes', methods=['GET'])
def dependentes():
    return render_template('CadastroDependentes.html')



if __name__ == '__main__':
    app.run(debug=True, port=5001)




