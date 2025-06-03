from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date
from database.db import Base
from sqlalchemy.orm import relationship

class ContaReceber(Base):
    __tablename__ = 'CONTAS_RECEBER'

    id = Column(Integer, primary_key=True)
    valor = Column(Float, nullable=False)
    dt_vencimento = Column(Date, nullable=False)
    metodo_pagamento = Column(String, nullable=False)
    n_parcelas = Column(Integer, nullable=False)
    status = Column(String, nullable=False)

    # FK para orçamento
    orcamento_id = Column(Integer, ForeignKey('ORCAMENTOS.id'))
    orcamento = relationship("Orcamento", back_populates="contas_receber")

    # FK para plano de pagamento
    plano_pagamento_id = Column(Integer, ForeignKey('PLANOS_PAGAMENTO.id'))
    plano_pagamento = relationship("PlanoPagamento", back_populates="contas_receber")
