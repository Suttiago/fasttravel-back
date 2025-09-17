from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from services.UserService import UserService
from database.db import get_db
from models.Usuario import Usuario
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token
from datetime import timedelta

user_bp = Blueprint('Usuario', __name__)
CORS(user_bp)
@user_bp.route('/CadastroUsuario', methods = ['POST'])
@cross_origin()
def criar_usuario():
    db =  next(get_db())
    service = UserService(db)
    data = request.get_json()
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


@user_bp.route('/Login', methods=['POST', 'GET'])
@cross_origin()
def login():
    db = next(get_db())
    service = UserService(db)

    data = request.get_json()
    email = data.get("email")
    senha = data.get("senha")

    usuario = service.autenticar(email, senha)

    if not usuario:
        return jsonify({"msg": "Credenciais inválidas"}), 401

    access_token = create_access_token(
        identity=str(usuario.id),  # <--- CONVERTA O ID PARA STRING
        additional_claims={"id": usuario.id, "email": usuario.email},
        expires_delta= timedelta(hours=1)
    )

    return jsonify({
        "msg": "Login realizado com sucesso",
        "access_token": access_token
    }), 200

@user_bp.route('/Listar', methods=['GET'])
@cross_origin()
def listar_usuario():
    db = next(get_db())
    service = UserService(db)
    usuarios = service.listar_todos()
    lista_usuarios = [d.to_dict() for d in usuarios]

    return jsonify(lista_usuarios), 200
