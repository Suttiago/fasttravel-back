from flask import Blueprint, jsonify
from database.db import get_db
from services.RelatorioService import RelatorioService
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin

relatorio_bp = Blueprint('relatorio', __name__)
CORS(relatorio_bp)


@relatorio_bp.route('/Financeiro', methods=['GET'])
@cross_origin()
@jwt_required()
def gerar_relatorio_financeiro_pdf():
    """
    Gera o mesmo relatório financeiro, mas retorna um PDF codificado em Base64.
    """
    db = next(get_db())
    service = RelatorioService(db)
    usuario_id = get_jwt_identity()

    if not usuario_id:
        return jsonify({'error': 'Usuário não identificado'}), 401

    # O serviço gera o HTML, converte para PDF e codifica em Base64
    pdf_base64 = service.gerar_relatorio_pdf_usuario(usuario_id)

    # Retorna a string Base64 dentro de um objeto JSON
    return jsonify({"pdf_base64": pdf_base64}), 200


@relatorio_bp.route('/Destino', methods=['GET'])
@cross_origin()
@jwt_required()
def gerar_relatorio_destino_pdf():
    """
    Gera o mesmo relatório financeiro, mas retorna um PDF codificado em Base64.
    """
    db = next(get_db())
    service = RelatorioService(db)
    usuario_id = get_jwt_identity()

    if not usuario_id:
        return jsonify({'error': 'Usuário não identificado'}), 401

    pdf_base64 = service.gerar_relatorio_destinos_pdf_usuario(usuario_id)

    return jsonify({"pdf_base64": pdf_base64}), 200
