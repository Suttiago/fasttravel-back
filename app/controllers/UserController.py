from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from services.UserService import UserService
from database.db import get_db
from models.Usuario import Usuario

user_bp = Blueprint('user', __name__)

@user_bp.route('/usuarios', methods = ['POST'])

def criar_usuario():
    db =  next(get_db())
    service = UserService(db)
    data = request.form
    usuario = Usuario(
        nome = data.get("nome"),
        email = data.get("email"),
        senha = data.get("senha"),
        cpf = data.get("cpf"),
        sexo = data.get("sexo"),
        profissao = data.get("profissao"),
        renda = data.get("renda"),
        data_nascimento = data.get("data_nascimento")
        
    )
    usuario_criado = service.salvar_usario(usuario)
    return jsonify(usuario_criado.to_dict()), 201


@user_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        db =  next(get_db())
        service = UserService(db)
        email = request.form('email')
        senha = request.form('senha') 
        usuario = service.autenticar(email,senha)
        if usuario:
            session['usuario.id'] = usuario.id
            flash('Login realizado com sucesso!!')
            return redirect(url_for('users'))       
        else:
            flash('Usuário ou senha incorretos')
    return render_template('login.html')
