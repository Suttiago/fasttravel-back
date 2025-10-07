from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from services.DestinoService import DestinoService
from database.db import get_db
from models.Destino import Destino
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_cors import CORS, cross_origin

destio_bp = Blueprint('destino',__name__)
CORS(destio_bp)

@destio_bp.route('/Cadastro', methods=['POST', 'OPTIONS'])
@jwt_required()
@cross_origin()
def novo_destino():
        db = next(get_db())
        service = DestinoService(db)
        data = request.get_json()
        destino = Destino(
            destino=data.get('destino'),
            check_in=data.get("check_in"),
            check_out=data.get("check_out"),
            adultos=data.get("adultos"),
            criancas=data.get("criancas"),
            status = "pendente",
            usuario_id=get_jwt_identity(),
            cidade_id = data.get("cidade_id")
        )
        destino_criado = service.salvar_destino(destino)
        return jsonify(destino_criado.to_dict()), 201
            

@destio_bp.route('/Listar', methods=['GET','POST','OPTIONS'])
@jwt_required()
@cross_origin()
def listar_destinos():
    usuario_id = get_jwt_identity()
    db = next(get_db())
    service = DestinoService(db)
    destinos = service.listar_destinos_por_usuario(usuario_id)
    lista_destinos = [d.to_dict() for d in destinos]
    return jsonify(lista_destinos)

@destio_bp.route('/Excluir/<int:destino_id>',methods=['DELETE'])
@jwt_required()
@cross_origin()
def excluir_destinos(destino_id):
    db = next(get_db())
    service = DestinoService(db)
    service.excluir_destino(destino_id)
    return jsonify({
        "message": "Destino excluído com sucesso!",
        "id": destino_id
    }), 200

@destio_bp.route('/Editar/<int:destino_id>',methods=['PUT'])
@jwt_required()
@cross_origin()
def editar_destinos(destino_id):
    db = next(get_db())
    service = DestinoService(db)
    data = request.get_json()
    service.editar_destinos(
        destino_id=destino_id,
        destino=data.get('destino'),
        check_in=data.get('check_in'),
        check_out=data.get('check_out'),
        adultos=data.get('adultos'),
        criancas=data.get('criancas'),
        status=data.get('status')
    )
    return jsonify({
        "message": "Destino editado com sucesso!",
        "id": destino_id
    }), 200
    
@destio_bp.route('/AceitarDest/<int:destino_id>',methods=['PUT'])
@jwt_required()
@cross_origin()
def aceitar_destino(destino_id):
    db = next(get_db())
    service = DestinoService(db)
    service.editar_destinos(
        status="Aceito"
    )
    return jsonify({
        "message": "Destino Aceito",
        "id": destino_id
    }), 200
    
@destio_bp.route('/RecusarDest/<int:destino_id>',methods=['PUT'])
@jwt_required()
@cross_origin()
def recusar_destino(destino_id):
    db = next(get_db())
    service = DestinoService(db)
    service.editar_destinos(
        status="Recusado"
    )
    return jsonify({
        "message": "Destino Aceito",
        "id": destino_id
    }), 200