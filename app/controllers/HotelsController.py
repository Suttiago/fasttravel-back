from flask import Blueprint, request, jsonify
from services.InfoHotelsService import HotelService
from models.InfoHotels import Hotels
from database.db import get_db
from models.Destino import Destino
from flask_cors import CORS,cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

hotel_bp = Blueprint("hotel", __name__)
CORS(hotel_bp)

@hotel_bp.route("/BuscarHoteis/<int:destino_id>", methods=["POST"])
@cross_origin()
@jwt_required()

def buscar_hoteis(destino_id):
    db = next(get_db())
    service = HotelService(db)
    destino = db.query(Destino).filter_by(id=destino_id).first()
    if not destino:
        return {"error": "Destino não encontrado"}, 404
    cidade = destino.destino  
    check_in = destino.check_in
    check_out = destino.check_out
    adultos = destino.adultos
    criancas = destino.criancas
    resultados = service.buscar_hoteis(
        cidade,
        check_in,
        check_out,
        adultos,
        criancas
    )
    
    return jsonify(resultados), 200

@hotel_bp.route("/SalvarHoteis", methods=["POST"])
@cross_origin()
@jwt_required()
def criar_hotel():
    db = next(get_db())
    service = HotelService(db)
    data = request.get_json()

    hotel = Hotels(
        hotel=data.get("hotel"),
        hotel_classification = data.get("hotel_classification"),
        hotel_description = data.get('hotel_description'),
        hotel_price = data.get('hotel_price'),
        destino_id = data.get('destino_id')
    )

    novo_hotel = service.salvar_hotel(hotel)
    return jsonify({"message": "Hotel cadastrado com sucesso!", "data": novo_hotel.to_dict()}), 201


@hotel_bp.route("/hoteis", methods=["GET"])
def listar_hoteis():
    db = next(get_db())
    service = HotelService(db)
    hoteis = service.listar_hoteis()
    return jsonify([h.to_dict() for h in hoteis]), 200

@hotel_bp.route("/ListarHoteisPorDestino/<int:destino_id>", methods=['GET','OPTIONS'])
@cross_origin()
@jwt_required()
def listar_por_destino(destino_id):
    db = next(get_db())
    service = HotelService(db)
    hoteis = service.listar_hoteis_por_destino(destino_id)
    return jsonify([h.to_dict() for h in hoteis]), 200
    


@hotel_bp.route("/hoteis/<int:hotel_id>", methods=["PUT"])
def editar_hotel(hotel_id):
    db = next(get_db())
    service = HotelService(db)
    data = request.get_json()

    hotel_editado = service.editar_hotel(
        hotel_id,
        data.get("nome"),
        data.get("localizacao"),
        data.get("check_in"),
        data.get("check_out"),
        data.get("preco_diaria")
    )

    if hotel_editado:
        return jsonify(hotel_editado.to_dict()), 200
    return jsonify({"error": "Hotel não encontrado"}), 404


@hotel_bp.route("/hoteis/<int:hotel_id>", methods=["DELETE"])
def excluir_hotel(hotel_id):
    db = next(get_db())
    service = HotelService(db)
    sucesso = service.excluir_hotel(hotel_id)

    if sucesso:
        return jsonify({"message": "Hotel excluído com sucesso!"}), 200
    return jsonify({"error": "Hotel não encontrado"}), 404
