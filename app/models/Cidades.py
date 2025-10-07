from sqlalchemy import Column, Integer, String
from database.db import Base
from sqlalchemy.orm import  relationship

class Cidades(Base):
    __tablename__ = 'CIDADES'
    
    id = Column(Integer, primary_key=True)
    nome= Column(String,nullable=False)
    codigo_iat= Column(String,nullable=False)
    
    destinos = relationship("Destino", back_populates="cidade")

    def to_dict(self):
        return{
            "id": self.id,  
            "nome": self.nome,
            "codigo_iat": self.codigo_iat
        }