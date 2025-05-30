from flask import Blueprint, request, jsonify
from services.DependenteService import DependenteService
from database.db import get_db
from models.Dependentes import Dependentes
user_bp = Blueprint('user', __name__)

@user_bp.route('/usuarios', methods = ['POST'])
def criar_dependente():
    db = next(get_db())
    service = DependenteService(db)
    data = request.form
    dependente = Dependentes(
        nome = data.get("nome"),
        cpf = data.get("cpf"),
        sexo = data.get("sexo"),
        data_nascimento = data.get("data_nascimento")   
    )
    depedente_criado = service.salvar_usario(dependente)
    return jsonify(depedente_criado.to_dict()), 201
