from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from services.DestinoService import DestinoService
from database.db import get_db
from models.Destino import Destino

destio_bp = Blueprint('destino',__name__)

@destio_bp.route('/CadastroDestino',methods=['POST','GET'])
def novo_destino():
    if not session.get('usuario_id'):
        flash('Você precisa estar logado para cadastrar um destino.')
        return redirect(url_for('user.login'))
    if request.method == 'POST':
        db =  next(get_db())
        service = DestinoService(db)
        data = request.form
        destino = Destino(
            destino = data.get('destino'),
            check_in = data.get("data_chegada"),
            check_out = data.get("data_saida"),
            adultos = data.get("adultos"),
            criancas = data.get("criancas"),
            usuario_id = session.get('usuario_id')
            
        )
        destino_criado = service.salvar_destino(destino)
        return jsonify(destino_criado.to_dict()), 201
    return render_template('CadastroDestino.html')

@destio_bp.route('/MeusDestinos')
def meus_destinos():
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        return redirect(url_for('user.login'))
    db = next(get_db())
    service = DestinoService(db)
    destinos = service.listar_destinos_por_usuario(usuario_id)
    return render_template('Destinos.html', destinos=destinos)

