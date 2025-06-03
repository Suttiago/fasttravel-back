from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database.db import Base
from sqlalchemy.orm import  relationship

class Orcamento(Base):
    __tablename__ = 'INFOHOTELS'
    
    id = Column(Integer, primary_key=True)
    hotel = Column(String,nullable=False)
    hotel_classification = Column(String,nullable=False)
    hotel_description = Column(String, nullable=False)
    hotel_price = Column(Float, nullable=False)
    
    usuario_id = Column(Integer,ForeignKey('USUARIOS.ID'),nullable=False)
    
    usuario = relationship("Usuario", back_populates="orcamentos")