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

    destinos = relationship("Destino", back_populates="info_hotels")

    def to_dict(self):
        """
        Converte uma instância da classe Hotels em um dicionário.
        """
        return {
            "id": self.id,
            "hotel": self.hotel,
            "hotel_classification": self.hotel_classification,
            "hotel_description": self.hotel_description,
            "hotel_price": self.hotel_price,
            "destino_id": self.destino_id,
        }