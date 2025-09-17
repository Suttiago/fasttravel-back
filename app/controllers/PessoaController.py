from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from models.Pessoa import Pessoa
from services.PessoaService import PessoaService
from database.db import get_db
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin
from datetime import datetime
pessoa_bp = Blueprint('pessoa', __name__)
CORS(pessoa_bp)

@pessoa_bp.route('/CadastroDependentes', methods=['GET', 'POST'])
@jwt_required()
@cross_origin()
def cadastrar_dependente():
    db = next(get_db())
    service = PessoaService(db)
    data = request.get_json()
    data_nascimento_str = data.get('data_nascimento')
    data_nascimento_obj = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
    dependente = Pessoa(
            nome = data.get('nome'),
            data_nascimento = data_nascimento_obj,
            cpf = data.get('cpf'),
            sexo = data.get('sexo'),
            responsavel_id = get_jwt_identity()

        )
    dependente_criado = service.criar_pessoa(dependente)
    return jsonify(dependente_criado.to_dict()), 201

@pessoa_bp.route('/Listar', methods=['GET','DELETE','PUT'])
@jwt_required()
@cross_origin()
def listar_dependentes():
    db = next(get_db())
    service = PessoaService(db)
    usuario_id = get_jwt_identity()
    dependentes = service.listar_dependentes(usuario_id)
    lista_dependentes = [d.to_dict() for d in dependentes]

    return jsonify(lista_dependentes)

@pessoa_bp.route('/ExcluirDependente/<int:dependente_id>',methods=['DELETE'])
@jwt_required()
@cross_origin()
def excluir_dependentes(dependente_id):
    db = next(get_db())
    service = PessoaService(db)
    service.excluir_dependentes(dependente_id)

    return jsonify({
        "message": "Dependente excluído com sucesso!",
        "id": dependente_id
    }), 200

@pessoa_bp.route('/EditarDependente/<int:dependente_id>',methods=['PUT'])
@jwt_required()
@cross_origin()
def editar_dependentes(dependente_id):
    db = next(get_db())
    service = PessoaService(db)
    data = request.get_json()
    service.editar_dependentes(
        dependente_id= dependente_id,
        nome = data.get('nome'),
        cpf=data.get('cpf'),    
        data_nascimento=data.get('data_nascimento')        
    )
    

    return jsonify({
        "message": "Dependente editado com sucesso!",
        "id": dependente_id
    }), 200