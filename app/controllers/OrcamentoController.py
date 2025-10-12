from flask import Blueprint, request, jsonify
from database.db import get_db
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin
from flask import Blueprint, request, jsonify
from services.OrcamentoService import OrcamentoService

orcamento_bp = Blueprint('orcamento', __name__)
CORS(orcamento_bp)


@orcamento_bp.route('/GerarOrcamento/<int:destino_id>', methods=['POST','OPTIONS'])
@cross_origin()
@jwt_required()
def gerar_orcamento(destino_id):
    db = next(get_db())
    service = OrcamentoService(db)
    orc = service.gerar_orcamento(destino_id)
    if not orc:
        return jsonify({'error': 'Não foi possível gerar o orçamento'}), 400
    return jsonify({'message': 'Orçamento gerado', 'orcamento': {
        'id': orc.id,
        'valor_passagens': orc.valor_passagens,
        'valor_hoteis': orc.valor_hoteis,
        'valor_total': orc.valor_total,
        'status': orc.status,
        'destino_id': orc.destino_id
    }}), 201


@orcamento_bp.route('/Listar', methods=['GET'])
@cross_origin()
@jwt_required()
def listar_orcamentos():
    db = next(get_db())
    service = OrcamentoService(db)
    orcamentos = service.listar_orcamentos()
    def to_dict(o):
        return {
            'id': o.id,
            'valor_passagens': o.valor_passagens,
            'valor_hoteis': o.valor_hoteis,
            'valor_total': o.valor_total,
            'status': o.status,
            'destino_id': o.destino_id
        }
    return jsonify([to_dict(o) for o in orcamentos]), 200


@orcamento_bp.route('/ListarPorDestino/<int:destino_id>', methods=['GET'])
@cross_origin()
@jwt_required()
def listar_por_destino(destino_id):
    db = next(get_db())
    service = OrcamentoService(db)
    orcamentos = service.listar_orcamento_dest(destino_id)
    def to_dict(o):
        return {
            'id': o.id,
            'valor_passagens': o.valor_passagens,
            'valor_hoteis': o.valor_hoteis,
            'valor_total': o.valor_total,
            'status': o.status,
            'destino_id': o.destino_id
        }
    return jsonify([to_dict(o) for o in orcamentos]), 200


@orcamento_bp.route('/Excluir/<int:orcamento_id>', methods=['DELETE'])
@cross_origin()
@jwt_required()
def excluir_orcamento(orcamento_id):
    db = next(get_db())
    service = OrcamentoService(db)
    sucesso = service.excluir_orcamento(orcamento_id)
    if sucesso:
        return jsonify({'message': 'Orçamento excluído', 'id': orcamento_id}), 200
    return jsonify({'error': 'Orçamento não encontrado'}), 404


@orcamento_bp.route('/Editar/<int:orcamento_id>', methods=['PUT'])
@cross_origin()
@jwt_required()
def editar_orcamento(orcamento_id):
    db = next(get_db())
    data = request.get_json()
    service = OrcamentoService(db)
    orc = service.editar_orcamento(orcamento_id, data.get('status'))
    if not orc:
        return jsonify({'error': 'Orçamento não encontrado'}), 404
    return jsonify({'message': 'Orçamento atualizado', 'id': orcamento_id}), 200
