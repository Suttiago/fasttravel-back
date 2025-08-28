from models.InfoFlights import Passagem
from sqlalchemy.orm import Session

class PassagemRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, passagem: Passagem):
        self.db.add(passagem)
        self.db.commit()
        self.db.refresh(passagem)
        return passagem

    def get_all(self):
        return self.db.query(Passagem).all()

    def get_by_id(self, passagem_id: int):
        return self.db.query(Passagem).filter(Passagem.id == passagem_id).first()

    def update(self, passagem_id: int, updated_data: dict):
        passagem = self.get_by_id(passagem_id)
        if passagem:
            for key, value in updated_data.items():
                setattr(passagem, key, value)
            self.db.commit()
            self.db.refresh(passagem)
        return passagem

    def delete(self, passagem_id: int):
        passagem = self.get_by_id(passagem_id)
        if passagem:
            self.db.delete(passagem)
            self.db.commit()
        return passagem
