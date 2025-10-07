from flask import Blueprint, request, jsonify
from services.CidadeService import CidadeService
from database.db import get_db
from models.Cidades import Cidades
from flask_jwt_extended import jwt_required
from flask_cors import CORS, cross_origin

cidade_bp = Blueprint('cidade', __name__)
CORS(cidade_bp)


@cidade_bp.route('/Cadastro', methods=['POST', 'OPTIONS'])
@jwt_required()
@cross_origin()
def novo_cidade():
    db = next(get_db())
    service = CidadeService(db)
    data = request.get_json()
    cidade = Cidades(
        nome=data.get('nome'),
        codigo_iat=data.get('codigo_iat')
    )
    cidade_criada = service.salvar_cidade(cidade)
    return jsonify({
        'id': cidade_criada.id,
        'nome': cidade_criada.nome,
        'codigo_iat': cidade_criada.codigo_iat
    }), 201


@cidade_bp.route('/Listar', methods=['GET', 'POST', 'OPTIONS'])
@jwt_required()
@cross_origin()
def listar_cidades():
    termo = request.args.get("termo", "")
    db = next(get_db())
    service = CidadeService(db)

    cidades = service.buscar_por_nome(termo)
    return jsonify([{"id": c.id, "nome": c.nome, "codigo_iat": c.codigo_iat} for c in cidades]), 200


@cidade_bp.route('/Excluir/<int:cidade_id>', methods=['DELETE'])
@jwt_required()
@cross_origin()
def excluir_cidade(cidade_id):
    db = next(get_db())
    service = CidadeService(db)
    sucesso = service.excluir_cidade(cidade_id)
    if sucesso:
        return jsonify({'message': 'Cidade excluída com sucesso!', 'id': cidade_id}), 200
    return jsonify({'message': 'Cidade não encontrada', 'id': cidade_id}), 404


@cidade_bp.route('/Editar/<int:cidade_id>', methods=['PUT'])
@jwt_required()
@cross_origin()
def editar_cidade(cidade_id):
    db = next(get_db())
    service = CidadeService(db)
    data = request.get_json()
    cidade = service.buscar_por_id(cidade_id)
    if not cidade:
        return jsonify({'message': 'Cidade não encontrada', 'id': cidade_id}), 404
    cidade.nome = data.get('nome', cidade.nome)
    cidade.codigo_iat = data.get('codigo_iat', cidade.codigo_iat)
    cidade_atualizada = service.editar_cidade(cidade)
    return jsonify({'message': 'Cidade editada com sucesso!', 'id': cidade_atualizada.id}), 200
