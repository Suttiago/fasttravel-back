from flask import Blueprint, request, jsonify
from service.InfoHotelsService import HotelService
from models.InfoHotels import Hotel
from database.db import get_db

hotel_bp = Blueprint("hotel", __name__)

@hotel_bp.route("/hoteis", methods=["POST"])
def criar_hotel():
    db = next(get_db())
    service = HotelService(db)
    data = request.get_json()

    hotel = Hotel(
        nome=data.get("nome"),
        localizacao=data.get("localizacao"),
        check_in=data.get("check_in"),
        check_out=data.get("check_out"),
        preco_diaria=data.get("preco_diaria"),
        usuario_id=data.get("usuario_id")
    )

    novo_hotel = service.salvar_hotel(hotel)
    return jsonify({"message": "Hotel cadastrado com sucesso!", "data": novo_hotel.to_dict()}), 201


@hotel_bp.route("/hoteis", methods=["GET"])
def listar_hoteis():
    db = next(get_db())
    service = HotelService(db)
    hoteis = service.listar_hoteis()
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
