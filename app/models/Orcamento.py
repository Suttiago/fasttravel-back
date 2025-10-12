from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database.db import Base
from sqlalchemy.orm import relationship
from models.ContaPagar import ContaPagar
class Orcamento(Base):
    __tablename__ = 'ORCAMENTOS'

    id = Column(Integer, primary_key=True)
    valor_passagens = Column(Float, nullable=False)
    valor_hoteis = Column(Float, nullable=False)
    valor_total = Column(Float, nullable=False)
    status = Column(String, nullable=False)

    destino_id = Column(Integer, ForeignKey('DESTINOS.id'))
    destinos = relationship("Destino", back_populates="orcamentos")

    contas_receber = relationship("ContaPagar", back_populates="orcamentos", cascade="all, delete-orphan")

  
