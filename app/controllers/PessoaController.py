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
        nome = request.form.get('nome')
        data_nascimento = request.form.get('data_nascimento')
        sexo = request.form.get('sexo')
        profissao = request.form.get('profissao')
        renda = request.form.get('renda')
        responsavel_id = request.form.get('responsavel_id')
        dependente = Pessoa(
            nome=nome,
            data_nascimento=data_nascimento,
            sexo=sexo,
            profissao=profissao,
            renda=renda,
            responsavel_id=responsavel_id
        )
        service.criar_pessoa(dependente)
        flash('Dependente cadastrado com sucesso!')
        return redirect(url_for('pessoa.cadastrar_dependente'))
    # Para GET, lista possíveis responsáveis
    pessoas = service.listar_pessoas()
    return render_template('CadastroDependentes.html', pessoas=pessoas)

@pessoa_bp.route('/MeusDependentes')
def meus_dependentes():
    db = next(get_db())
    service = PessoaService(db)
    usuario_id = session.get('usuario_id')
    dependentes = service.listar_dependentes(usuario_id)
    return render_template('MeusDependentes.html', dependentes=dependentes)