from models.Destino import Destino

class DestinoRepository:
    def __init__(self,db):
        self.db = db
    
    def criar_destino(self, destino : Destino):
        self.db.add(destino)
        self.db.commit()
        self.db.refresh(destino)
        return destino

    def listar_destinos(self, destino:Destino):
        self.db.query(destino).filter_by(destino.id).first()
        
    def editar_destinos(self, destino:Destino):
        destino_db = self.db.query(Destino).filter_by(id=destino.id)
        if destino_db:
            destino_db.check_in= destino.check_in
            destino_db.check_out = destino.check_out
            destino_db.criancas  = destino.criancas
            destino_db.adultos = destino.adultos
            destino_db.usuario_id= destino.usuario_id
            self.db.commit()
            self.db.refresh(destino_db)
            return destino_db
        
    
    def excluir_destinos(self, destino_id):
        destino_db = self.db.query(Destino).filter_by(id=destino_id).first()
        if destino_db:
            self.db.delete(destino_db)
            self.db.commit()
            return True
        return False
    
    def buscar_email(self, email):
        return self.db.query(Destino).filter_by(email=email).first