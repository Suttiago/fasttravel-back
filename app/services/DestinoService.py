from models.Destino import Destino
from repository.DestinoRepository import DestinoRepository

class DestinoService:
    def __init__(self, db):
        self.db = db
        self.repo = DestinoRepository(db)
        
    def salvar_destino(self, destino: Destino):
        return self.repo.criar_destino(destino)
    
    def listar_destino(self, destino: Destino):
        return self.repo.listar_destinos(destino)
    
    def listar_destinos_por_usuario(self, usuario_id):
        return self.db.query(Destino).filter_by(usuario_id=usuario_id).all()

    def editar_destino(self,destino: Destino):
        return self.repo.editar_destinos(destino)
        
    def excluir_destino(self, destino: Destino):
        return self.repo.excluir_destinos(destino)