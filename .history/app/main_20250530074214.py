from flask import Blueprint, render_template, request, redirect, url_for, app,Flask
from projeto_viagens.app.controllers.UserController import user_bp

app = Flask(__name__, template_folder="templates")

app.register_blueprint(user_bp)

@app.route('/usuarios', methods=['GET'])
def users():
    return render_template('cadastro.html')

@app.route('/CadastroDependentes', methods=['GET'])
def dependentes():
    return render_template('CadastroDependentes.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)




