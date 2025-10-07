from models.InfoFlights import Passagem
from sqlalchemy.orm import Session

class PassagemRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar_passagem(self, passagem: Passagem):
        self.db.add(passagem)
        self.db.commit()
        self.db.refresh(passagem)
        return passagem

    def listar_passagens(self):
        return self.db.query(Passagem).all()

    def listar_passagens_por_id(self, passagem_id: int):
        return self.db.query(Passagem).filter(Passagem.id == passagem_id).first()

    def editar_passagem(self, passagem_id: int, updated_data: dict):
        passagem = self.get_by_id(passagem_id)
        if passagem:
            for key, value in updated_data.items():
                setattr(passagem, key, value)
            self.db.commit()
            self.db.refresh(passagem)
        return passagem

    def excluir_passagem(self, passagem_id: int):
        passagem = self.get_by_id(passagem_id)
        if passagem:
            self.db.delete(passagem)
            self.db.commit()
        return passagem
