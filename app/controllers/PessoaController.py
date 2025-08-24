from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.Pessoa import Pessoa
from services.PessoaService import PessoaService
from database.db import get_db

pessoa_bp = Blueprint('pessoa', __name__)

@pessoa_bp.route('/CadastroDependentes', methods=['GET', 'POST'])
def cadastrar_dependente():
    db = next(get_db())
    service = PessoaService(db)
    if request.method == 'POST':
        dependente = Pessoa(
            nome = request.form.get('nome'),
            data_nascimento = request.form.get('data_nascimento'),
            cpf = request.form.get('cpf'),
            sexo = request.form.get('sexo'),
            responsavel_id = session.get('usuario_id')
        )
        service.criar_pessoa(dependente)
        flash('Dependente cadastrado com sucesso!')
        return redirect(url_for('index'))
    # Para GET, lista possíveis responsáveis
    return render_template('CadastroDependentes.html')

@pessoa_bp.route('/Dependentes')
def meus_dependentes():
    db = next(get_db())
    service = PessoaService(db)
    usuario_id = session.get('usuario_id')
    dependentes = service.listar_dependentes(usuario_id)
    return render_template('Dependentes.html', dependentes=dependentes)

@pessoa_bp.route('/ExcluirDependente/<int:dependente_id>',methods=['POST'])
def excluir_dependentes(dependente_id):
    db = next(get_db())
    service = PessoaService(db)
    service.excluir_dependentes(dependente_id)
    flash('Destino excluído com sucesso!')
    return redirect(url_for('pessoa.listar_dependentes'))