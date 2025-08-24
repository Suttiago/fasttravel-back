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

    def editar_destinos(self, destino_id, destino, check_in, check_out, adultos, criancas, status):
        destino_db = self.db.query(Destino).filter_by(id=destino_id).first()
        if destino_db:
            destino_db.destino = destino
            destino_db.check_in = check_in
            destino_db.check_out = check_out
            destino_db.adultos = adultos
            destino_db.criancas = criancas
            destino_db.status = status
            self.db.commit()
            self.db.refresh(destino_db)
            return destino_db
        return None
        
    def excluir_destino(self, destino_id):
        return self.repo.excluir_destinos(destino_id)