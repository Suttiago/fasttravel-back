from sqlalchemy import Column, Integer, Date, String,Float, ForeignKey
from database.db import Base
from sqlalchemy.orm import  relationship
class Passagem(Base):
    __tablename__ = 'INFOFLIGHTS'
    
    id = Column(Integer, primary_key=True)
    aeroporto_saida= Column(String,nullable=False)
    aeroporto_chegada = Column(String,nullable=False)
    aviao = Column(String, nullable=False)
    linha_aerea = Column(String, nullable=False)
    preco_passagem = Column(Float, nullable=False)
    destino_id = Column(Integer, ForeignKey('DESTINOS.id'))
    
    destinos = relationship("Destino", back_populates="info_flights")
    def to_dict(self):
        """Converte uma instância de Passagem em dicionário."""
        return {
            "id": self.id,
            "aeroporto_saida": self.aeroporto_saida,
            "aeroporto_chegada": self.aeroporto_chegada,
            "aviao": self.aviao,
            "linha_aerea": self.linha_aerea,
            "preco_passagem": self.preco_passagem,
            "destino_id": self.destino_id,
        }