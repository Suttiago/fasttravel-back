from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date
from database.db import Base
from sqlalchemy.orm import relationship

class ContaPagar(Base):
    __tablename__ = 'CONTAS_PAGAR'

    id = Column(Integer, primary_key=True)
    valor = Column(Float, nullable=False)
    dt_vencimento = Column(Date, nullable=False)
    metodo_pagamento = Column(String, nullable=False)
    instituicao_pagamento = Column(String, nullable=True)
    n_parcelas = Column(Integer, nullable=False)
    status = Column(String, nullable=False)

    orcamento_id = Column(Integer, ForeignKey('ORCAMENTOS.id'))
    orcamentos = relationship("Orcamento", back_populates="contas_receber")
    
    def to_dict(self):
        """Converte uma instância de Passagem em dicionário."""
        return {
            "id": self.id,
            "valor": self.valor,
            "dt_vencimento": self.dt_vencimento,
            "metodo_pagamento": self.metodo_pagamento,
            "instituicao_pagamento": self.instituicao_pagamento,
            "n_parcelas": self.n_parcelas,
            "status": self.status,
        }
