from sqlalchemy import Column, Integer, Date, String
from database.db import Base

class Orcamento(Base):
    __tablename__ = 'ORCAMENTOS'
    
    id = Column(Integer, primary_key=True)
    check_in = Column(Date,nullable=False)
    check_out = Column(Date,nullable=False)
    adultos = Column(Integer, nullable=False)
    criancas = Column(Integer, nullable=False)
    Status = Column(String, nullable=False)