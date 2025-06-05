from sqlalchemy import Column, Integer, String
from database.db import Base
from sqlalchemy.orm import relationship
class PlanoPagamento(Base):
    __tablename__ = 'PLANOS_PAGAMENTO'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    instituicao_pagamento = Column(String, nullable=False)
    conta_bancaria = Column(String, nullable=False)

    # Relacionamento com ContaReceber
    contas_receber = relationship("ContaReceber", back_populates="plano_pagamento")
