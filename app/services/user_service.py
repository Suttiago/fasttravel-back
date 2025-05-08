from models.user import Usuario
from repository.user_repository import User_repository
 
class User_service:
    def __init__(self):
        self.repo = User_repository()
        
        
    def criar_usuario(self, usuario:Usuario):
        self.repo.inserir_usuario(usuario)
        
    def excluir_usuario(self,usuario:Usuario):
        self.repo.deletar_usuario(usuario)
        
    def editar_usuario(self, usuario:Usuario):
        self.repo.update_usuario(usuario)
        
    def listar_usuario(self,usuario:Usuario):
        self.repo.selecionar_usuarios(usuario)