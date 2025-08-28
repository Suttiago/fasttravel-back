from models.Passagem import Passagem
from repository.PassagemRepository import PassagemRepository

class PassagemService:
    def __init__(self, db):
        self.db = db
        self.repo = PassagemRepository(db)

    def salvar_passagem(self, passagem: Passagem):
        return self.repo.criar_passagem(passagem)
    
    def listar_passagens(self):
        return self.repo.listar_passagens()

    def listar_passagens_por_destino(self, destino_id):
        return self.db.query(Passagem).filter_by(destino_id=destino_id).all()

    def editar_passagem(self, passagem_id, origem, destino, preco, disponibilidade):
        passagem_db = self.db.query(Passagem).filter_by(id=passagem_id).first()
        if passagem_db:
            passagem_db.origem = origem
            passagem_db.destino = destino
            passagem_db.preco = preco
            passagem_db.disponibilidade = disponibilidade
            self.db.commit()
            self.db.refresh(passagem_db)
            return passagem_db
        return None
    
    def excluir_passagem(self, passagem_id):
        return self.repo.excluir_passagem(passagem_id)
