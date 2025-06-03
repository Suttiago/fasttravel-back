from models.Usuario import Usuario
from repository.UserRepository import UserRepository
 
class UserService:
    def __init__(self, db):
        self.repo = UserRepository(db)
        
    def salvar_usario(self, usuario:Usuario):
        return self.repo.criar_usuario(usuario)
    
    def listar_usuario(self,usuario:Usuario):
        return self.repo.listar_usuarios(usuario)
        
    def editar_usuario(self, usuario:Usuario):
        return self.repo.editar_usuario(usuario)
        
    def excluir_usuario(self,usuario:Usuario):
        return self.repo.excluir_usuario(usuario)
        
    def autenticar(self,email,senha):
        usuario = self.repo.buscar_email(email)
        if usuario and usuario.senha ==senha:
            return usuario
        return None
        
        