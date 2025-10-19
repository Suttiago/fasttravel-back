from flask import Blueprint, request, jsonify
from database.db import get_db
from services.PlanoPagamentoService import PlanoPagamentoService
from models.PlanoPagamento import PlanoPagamento
from flask_jwt_extended import jwt_required
from flask_cors import CORS, cross_origin
from datetime import datetime

plano_bp = Blueprint('plano', __name__)
CORS(plano_bp)

@plano_bp.route('/Criar', methods=['POST'])
@cross_origin()
@jwt_required()
def criar_novo_plano():
    """Cria um novo plano de pagamento a partir dos dados recebidos via JSON."""
    db = next(get_db())
    service = PlanoPagamentoService(db)
    data = request.get_json()

    dt_pagamento_str = data.get('dt_pagamento')
    dt_pagamento_obj = datetime.strptime(dt_pagamento_str, '%Y-%m-%d').date() if dt_pagamento_str else None

    novo_plano = PlanoPagamento(
        nome=data.get('nome'),
        tipo=data.get('tipo'),
        instituicao_pagamento=data.get('instituicao_pagamento'),
        conta_bancaria=data.get('conta_bancaria'),
        numero_cartao=data.get('numero_cartao'),
        nome_titular=data.get('nome_titular'),
        dt_validade_cartao=data.get('dt_validade_cartao'),
        cvv=data.get('cvv'),
        valor_pagamento=data.get('valor_pagamento'),
        dt_pagamento=dt_pagamento_obj,
        contas_pagar_id=data.get('conta_pagar_id')
    )

    plano_criado = service.criar_novo_plano(novo_plano)
    
    # Retorna o plano criado como um dicionário JSON
    return jsonify(plano_criado.to_dict()), 201


@plano_bp.route('/Listar', methods=['GET'])
@cross_origin()
@jwt_required()
def listar_todos_planos():
    """Lista todos os planos de pagamento existentes."""
    db = next(get_db())
    service = PlanoPagamentoService(db)
    planos = service.listar_todos_planos()
    return jsonify([p.to_dict() for p in planos]), 200


@plano_bp.route('/Buscar/<int:plano_id>', methods=['GET'])
@cross_origin()
@jwt_required()
def buscar_plano_por_id(plano_id: int):
    """Busca um plano de pagamento pelo seu ID."""
    db = next(get_db())
    service = PlanoPagamentoService(db)
    plano = service.buscar_plano_por_id(plano_id)
    if not plano:
        return jsonify({'error': 'Plano de pagamento não encontrado'}), 404
    return jsonify(plano.to_dict()), 200


@plano_bp.route('/BuscarPorConta/<int:conta_id>', methods=['GET'])
@cross_origin()
@jwt_required()
def buscar_plano_por_conta_id(conta_id: int):
    """Busca um plano de pagamento pelo ID da conta associada."""
    db = next(get_db())
    service = PlanoPagamentoService(db)
    plano = service.buscar_plano_por_conta_id(conta_id)
    if not plano:
        return jsonify({'error': 'Nenhum plano de pagamento encontrado para esta conta'}), 404
    return jsonify(plano.to_dict()), 200


@plano_bp.route('/Editar/<int:plano_id>', methods=['PUT'])
@cross_origin()
@jwt_required()
def atualizar_plano(plano_id: int):
    """Atualiza um plano de pagamento existente."""
    db = next(get_db())
    service = PlanoPagamentoService(db)
    data = request.get_json()

    plano_atualizado = service.atualizar_plano(plano_id, data)
    if not plano_atualizado:
        return jsonify({'error': 'Plano de pagamento não encontrado'}), 404
    return jsonify(plano_atualizado.to_dict()), 200


@plano_bp.route('/Excluir/<int:plano_id>', methods=['DELETE'])
@cross_origin()
@jwt_required()
def remover_plano(plano_id: int):
    """Exclui um plano de pagamento."""
    db = next(get_db())
    service = PlanoPagamentoService(db)
    sucesso = service.remover_plano(plano_id)
    if not sucesso:
        return jsonify({'error': 'Plano de pagamento não encontrado'}), 404
    return jsonify({'message': 'Plano de pagamento excluído com sucesso'}), 200
