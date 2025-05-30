from flask import Blueprint, request, jsonify
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
