from flask import Blueprint, request, jsonify
from services.InfoFlightsService import PassagemService
from models.InfoFlights import Passagem
from database.db import get_db
from models.Destino import Destino
from flask_cors import CORS, cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

passagem_bp = Blueprint("passagem", __name__)
CORS(passagem_bp)


@passagem_bp.route("/BuscarPassagens/<int:destino_id>", methods=["POST"])
@cross_origin()
@jwt_required()
def buscar_passagens(destino_id):
    db = next(get_db())
    service = PassagemService(db)
    destino = db.query(Destino).filter_by(id=destino_id).first()
    if not destino:
        return {"error": "Destino não encontrado"}, 404
    codigo_iat = destino.cidade.codigo_iat if getattr(destino, 'cidade', None) else None
    check_in = destino.check_in
    check_out = destino.check_out
    resultados = service.buscar_passagem(
        codigo_iat,
        check_in,
        check_out
    )
    return jsonify(resultados), 200


@passagem_bp.route("/SalvarPassagens", methods=["POST"])
@cross_origin()
@jwt_required()
def criar_passagem():
    db = next(get_db())
    service = PassagemService(db)
    data = request.get_json()

    passagem = Passagem(
        aeroporto_saida=data.get("aeroporto_saida"),
        aeroporto_chegada=data.get("aeroporto_chegada"),
        aviao=data.get('aviao'),
        linha_aerea=data.get('linha_aerea'),
        preco_passagem=data.get('preco_passagem'),
        destino_id=data.get('destino_id')   
    )

    nova_passagem = service.salvar_passagem(passagem)
    return jsonify({"message": "Passagem cadastrada com sucesso!", "data": nova_passagem.to_dict()}), 201


@passagem_bp.route("/passagens", methods=["GET"])
def listar_passagens():
    db = next(get_db())
    service = PassagemService(db)
    passagens = service.listar_passagens()
    return jsonify([p.to_dict() for p in passagens]), 200


@passagem_bp.route("/ListarPassagensPorDestino/<int:destino_id>", methods=['GET','OPTIONS'])
@cross_origin()
@jwt_required()
def listar_por_destino(destino_id):
    db = next(get_db())
    service = PassagemService(db)
    passagens = service.listar_passagens_por_destino(destino_id)
    return jsonify([p.to_dict() for p in passagens]), 200


@passagem_bp.route("/passagens/<int:passagem_id>", methods=["PUT"])
def editar_passagem(passagem_id):
    db = next(get_db())
    service = PassagemService(db)
    data = request.get_json()

    passagem_editada = service.editar_passagem(
        passagem_id,
        data.get("aeroporto_saida"),
        data.get("aeroporto_chegada"),
        data.get("preco_passagem"),
        data.get("disponibilidade")
    )

    if passagem_editada:
        return jsonify(passagem_editada.to_dict()), 200
    return jsonify({"error": "Passagem não encontrada"}), 404


@passagem_bp.route("/passagens/<int:passagem_id>", methods=["DELETE"])
def excluir_passagem(passagem_id):
    db = next(get_db())
    service = PassagemService(db)
    sucesso = service.excluir_passagem(passagem_id)

    if sucesso:
        return jsonify({"message": "Passagem excluída com sucesso!"}), 200
    return jsonify({"error": "Passagem não encontrada"}), 404
