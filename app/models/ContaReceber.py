from sqlalchemy import Column, Integer, Date, String, Float
from database.db import Base

class ContaReceber(Base):
    __tablename__ = 'CONTAS_RECEBER'
    
    id = Column(Integer, primary_key = True)
    valor = Column(Float, nullable=True)
    dt_vencimento = Column(Date, nullable=True)
    tipo_pagamento = Column(String, nullable= True)
    numero_parcelas = Column(Float, nullable=True)
    status = Column(String, nullable=True)