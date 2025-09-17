import bcrypt
from models.Usuario import Usuario
from repository.UserRepository import UserRepository
 
class UserService:
    def __init__(self, db):
        self.repo = UserRepository(db)
        
    def salvar_usario(self, usuario:Usuario):
        senha_hash = bcrypt.hashpw(usuario.senha.encode('utf-8'), bcrypt.gensalt())
        usuario.senha = senha_hash.decode('utf-8')
        return self.repo.criar_usuario(usuario)
    
    def listar_usuario(self,usuario:Usuario):
        return self.repo.listar_usuarios(usuario)
        
    def listar_todos(self):
        return self.repo.listar_tudo()
        
    def editar_usuario(self, usuario:Usuario):
        return self.repo.editar_usuario(usuario)
        
    def excluir_usuario(self,usuario:Usuario):
        return self.repo.excluir_usuario(usuario)
        

    def autenticar(self, email: str, senha: str):
        usuario = self.repo.buscar_email(email)
        if not usuario:
            return None
        if bcrypt.checkpw(senha.encode('utf-8'), usuario.senha.encode('utf-8')):
            return usuario
        return None
        
        