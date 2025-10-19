from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from services.ContaPagarService import ContaPagarService
from database.db import get_db
from models.ContaPagar import ContasPagar 
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_cors import CORS, cross_origin
from datetime import date, timedelta

pagar_bp = Blueprint('conta',__name__)
CORS(pagar_bp)

@pagar_bp.route('/CadastrarContas', methods=['POST', 'OPTIONS'])
@jwt_required()
@cross_origin()
def nova_conta():
        db = next(get_db())
        service = ContaPagarService(db)
        data = request.get_json()
        sysdate = date.today()
        numero_parcelas = int(data.get("numero_parcelas", 1))
        contaPagar = ContasPagar(
            valor = data.get("valor_total"),
            dt_vencimento =  sysdate + timedelta(days=30),
            instituicao_pagamento = data.get("banco"),
            metodo_pagamento = data.get("metodo_pagamento"),
            n_parcelas = numero_parcelas,
            status = "pendente",
            orcamento_id = data.get("orcamento_id")
                    
        )
        contas_criadas = service.criar_nova_conta(contaPagar,numero_parcelas)
        
        return jsonify([c.to_dict() for c in contas_criadas]), 201   


@pagar_bp.route('/Listar/<int:conta_id>', methods=['GET', 'OPTIONS'])
@jwt_required()
@cross_origin()
def listar_conta(conta_id):
        db = next(get_db())
        service = ContaPagarService(db)
        contas_pagar = service.listar_contas_por_orcamento(conta_id)
        lista_contas = [c.to_dict() for c in contas_pagar]
        return jsonify(lista_contas)
    
@pagar_bp.route('/Editar/<int:conta_id>', methods=['PUT'])
@cross_origin()
@jwt_required()
def editar_orcamento(conta_id):
    db = next(get_db())
    data = request.get_json()
    service = ContaPagarService(db)
    service.atualizar_status_pagamento(
        conta_id, data.get('status')
    )

    return jsonify({'message': 'Orçamento atualizado', 'id': conta_id}), 200
