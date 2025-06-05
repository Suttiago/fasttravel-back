from sqlalchemy import Column, Integer, Date, String, ForeignKey
from database.db import Base
from sqlalchemy.orm import  relationship
from models.InfoFlights import Passagem
from models.InfoHotels import Hotels
from models.Orcamento import Orcamento
class Destino(Base):
    __tablename__ = 'DESTINOS'
    
    id = Column(Integer, primary_key=True)
    destino = Column(String, nullable=False)
    check_in = Column(Date,nullable=False)
    check_out = Column(Date,nullable=False)
    adultos = Column(Integer, nullable=False)
    criancas = Column(Integer, nullable=False)
    status = Column(String, nullable=True)    
    usuario_id = Column(Integer,ForeignKey('USUARIOS.id'),nullable=False)
    
    usuario = relationship("Usuario", back_populates="destinos")
    info_flights = relationship("Passagem", back_populates="destinos", cascade="all, delete-orphan")
    info_hotels = relationship("Hotels", back_populates="destinos", cascade="all, delete-orphan")
    orcamentos = relationship("Orcamento", back_populates="destinos", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "destino": self.destino,
            "check_in": str(self.check_in),
            "check_out": str(self.check_out),
            "adultos": self.adultos,
            "criancas": self.criancas,
            "status": getattr(self, "status", None),
            "usuario_id": self.usuario_id
        }

