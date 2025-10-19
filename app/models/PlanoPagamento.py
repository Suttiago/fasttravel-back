from sqlalchemy import Column, Integer, String, Float, Date,ForeignKey
from database.db import Base
from sqlalchemy.orm import relationship
class PlanoPagamento(Base):
    __tablename__ = 'PLANOS_PAGAMENTO'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    instituicao_pagamento = Column(String, nullable=False)
    conta_bancaria = Column(String, nullable=False)
    numero_cartao = Column(String, nullable=True)
    nome_titular = Column(String, nullable=True)
    dt_validade_cartao= Column(String,nullable=True)
    cvv = Column(String,nullable=True)
    valor_pagamento = Column(Float,nullable=False)
    dt_pagamento = Column(Date,nullable=False)
    
    contas_pagar_id = Column(Integer, ForeignKey('CONTAS_PAGAR.id'), nullable=False)
    contas_pagar = relationship("ContasPagar", back_populates="plano_pagamento")
    
    def to_dict(self):
        """Converte uma instância de PlanoPagamento em um dicionário serializável."""
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo,
            "instituicao_pagamento": self.instituicao_pagamento,
            "conta_bancaria": self.conta_bancaria,
            "numero_cartao": self.numero_cartao,
            "nome_titular": self.nome_titular,
            "dt_validade_cartao": self.dt_validade_cartao,
            "cvv": self.cvv,
            # Converte de Decimal para float para ser compatível com JSON
            "valor_pagamento": float(self.valor_pagamento) if self.valor_pagamento is not None else 0.0,
            # Converte a data para string no formato AAAA-MM-DD
            "dt_pagamento": self.dt_pagamento.isoformat() if self.dt_pagamento else None,
            "contas_pagar_id": self.contas_pagar_id
        }