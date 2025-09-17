from models.Usuario import Usuario

class UserRepository:
    def __init__(self,db):
        self.db = db
    
    def criar_usuario(self, usuario : Usuario):
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def listar_usuarios(self, usuario: Usuario):
        self.db.query(usuario).filter_by(usuario.id).first()
        
    def listar_tudo(self):
        return self.db.query(Usuario).all()
        
    def editar_usuario(self, usuario:Usuario):
        usuario_db = self.db.query(Usuario).filter_by(id=usuario.id)
        if usuario_db:
            usuario_db.email = usuario.email
            usuario_db.senha = usuario.senha
            usuario_db.nome  = usuario.nome
            usuario_db.data_nascimento = usuario.data_nascimento
            usuario_db.sexo = usuario.sexo
            usuario_db.profissao = usuario.profissao
            usuario_db.renda = usuario.renda
            self.db.commit()
            self.db.refresh(usuario_db)
            return usuario_db
        
    
    def excluir_usuario(self, usuario: Usuario):
        usuario_db = self.db.query(Usuario).filter_by(id=usuario.id).first()
        if usuario_db:
            self.db.delete(usuario_db)
            self.db.commit()
            return True
        return False
    
    def buscar_email(self, email):
        return self.db.query(Usuario).filter_by(email=email).first()