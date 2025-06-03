from sqlalchemy import Column, Integer, Date, String, ForeignKey
from database.db import Base
from sqlalchemy.orm import  relationship

class Orcamento(Base):
    __tablename__ = 'ORCAMENTOS'
    
    id = Column(Integer, primary_key=True)
    check_in = Column(Date,nullable=False)
    check_out = Column(Date,nullable=False)
    adultos = Column(Integer, nullable=False)
    criancas = Column(Integer, nullable=False)
    Status = Column(String, nullable=False)
    
    usuario_id = Column(Integer,ForeignKey('USUARIOS.ID'),nullable=False)
    usuario = relationship("Usuario", back_populates="orcamentos")

    destino_id = Column(Integer, ForeignKey('DESTINOS.id'))
    destino = relationship("Destino", back_populates="orcamentos")
