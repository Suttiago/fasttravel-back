from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database.db import Base
from sqlalchemy.orm import  relationship

class Hotels(Base):
    __tablename__ = 'INFOHOTELS'
    
    id = Column(Integer, primary_key=True)
    hotel = Column(String,nullable=False)
    hotel_classification = Column(String,nullable=False)
    hotel_description = Column(String, nullable=False)
    hotel_price = Column(Float, nullable=False)
    destino_id = Column(Integer, ForeignKey('DESTINOS.id'))

    destino = relationship("Destino", back_populates="info_flights")
