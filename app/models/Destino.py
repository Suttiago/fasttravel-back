from sqlalchemy import Column, Integer, Date, String, ForeignKey
from database.db import Base
from sqlalchemy.orm import  relationship

class Destino(Base):
    __tablename__ = 'DESTINOS'
    
    id = Column(Integer, primary_key=True)
    check_in = Column(Date,nullable=False)
    check_out = Column(Date,nullable=False)
    adultos = Column(Integer, nullable=False)
    criancas = Column(Integer, nullable=False)
    Status = Column(String, nullable=False)    
    usuario_id = Column(Integer,ForeignKey('USUARIOS.ID'),nullable=False)
    
    usuario = relationship("Usuario", back_populates="destinos")

    info_flights = relationship("InfoFlights", back_populates="destino", cascade="all, delete-orphan")

    info_hotels = relationship("InfoHotels", back_populates="destino", cascade="all, delete-orphan")

    orcamentos = relationship("Orcamento", back_populates="destino", cascade="all, delete-orphan")
