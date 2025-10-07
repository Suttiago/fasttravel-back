from flask import Blueprint, request, jsonify
from database.db import get_db
from models.Orcamento import Orcamento
from models.Destino import Destino
from services.InfoFlightsService import PassagemService
from services.InfoHotelsService import HotelService
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin

orcamento_bp = Blueprint('orcamento', __name__)
CORS(orcamento_bp)


@orcamento_bp.route('/GerarOrcamento/<int:destino_id>', methods=['POST'])
@cross_origin()
@jwt_required()
def gerar_orcamento(destino_id):
    db = next(get_db())
    user_id = get_jwt_identity()

    passagem_service = PassagemService(db)
    hotel_service = HotelService(db)

    passagens = passagem_service.listar_passagens_por_destino(destino_id)
    hoteis = hotel_service.listar_hoteis_por_destino(destino_id)

    total_passagens = sum([p.preco_passagem or 0 for p in passagens])
    total_hoteis = sum([h.hotel_price or 0 for h in hoteis])
    valor_total = total_passagens + total_hoteis

    orcamento = Orcamento(
        valor_passagens=total_passagens,
        valor_hoteis=total_hoteis,
        valor_total=valor_total,
        status='pendente',
        destino_id=destino_id
    )
    db.add(orcamento)
    db.commit()
    db.refresh(orcamento)

    return jsonify({
        'message': 'Orçamento gerado',
        'orcamento': {
            'id': orcamento.id,
            'valor_passagens': orcamento.valor_passagens,
            'valor_hoteis': orcamento.valor_hoteis,
            'valor_total': orcamento.valor_total,
            'status': orcamento.status,
            'destino_id': orcamento.destino_id
        }
    }), 201


@orcamento_bp.route('/Listar', methods=['GET'])
@cross_origin()
@jwt_required()
def listar_orcamentos():
    db = next(get_db())
    orcamentos = db.query(Orcamento).all()
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
    orc = db.query(Orcamento).filter_by(id=orcamento_id).first()
    db.delete(orc)
    db.commit()
    return jsonify({'message': 'Orçamento excluído', 'id': orcamento_id}), 200


@orcamento_bp.route('/Editar/<int:orcamento_id>', methods=['PUT'])
@cross_origin()
@jwt_required()
def editar_orcamento(orcamento_id):
    db = next(get_db())
    data = request.get_json()
    orc = db.query(Orcamento).filter_by(id=orcamento_id).first()
    orc.status = data.get('status', orc.status)
    db.commit()
    db.refresh(orc)
    return jsonify({'message': 'Orçamento atualizado', 'id': orcamento_id}), 200
