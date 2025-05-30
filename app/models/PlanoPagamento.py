from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class PlanoPagamento(Base):
    __tablename__ = 'PLANO_PAGAMENTO'
    
    id = Column(Integer, primary_key = True)
    nome = Column(String, nullable= True)
    tipo = Column(String, nullable= True)
    quantidade_parcelas = Column(Float, nullable=True)
    
    