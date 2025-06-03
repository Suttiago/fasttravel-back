from flask import Blueprint, request, jsonify
from services.DependenteService import DependenteService
from database.db import get_db
from models.Dependentes import Dependentes

dependente_bp = Blueprint('dependente', __name__)

@dependente_bp.route('/CadastroDependentes', methods = ['POST'])
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
    depedente_criado = service.salvar_dependente(dependente)
    return jsonify(depedente_criado.to_dict()), 201
