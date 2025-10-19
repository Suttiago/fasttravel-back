from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database.db import Base
from sqlalchemy.orm import relationship
from models.ContaPagar import ContasPagar
class Orcamento(Base):
    __tablename__ = 'ORCAMENTOS'

    id = Column(Integer, primary_key=True)
    valor_passagens = Column(Float, nullable=False)
    valor_hoteis = Column(Float, nullable=False)
    valor_total = Column(Float, nullable=False)
    status = Column(String, nullable=False)

    destino_id = Column(Integer, ForeignKey('DESTINOS.id'))
    destinos = relationship("Destino", back_populates="orcamentos")
    usuario_id = Column(Integer, ForeignKey('USUARIOS.id'), nullable=False)
    usuario = relationship("Usuario", back_populates="orcamentos")

    contas_receber = relationship("ContasPagar", back_populates="orcamentos", cascade="all, delete-orphan")

    def to_dict(self):
        """Converte uma instância de Orcamento em um dicionário serializável."""
        return {
            "id": self.id,
            # Converte de Decimal (Numeric) para float para ser compatível com JSON
            "valor_passagens": float(self.valor_passagens) if self.valor_passagens is not None else 0.0,
            "valor_hoteis": float(self.valor_hoteis) if self.valor_hoteis is not None else 0.0,
            "valor_total": float(self.valor_total) if self.valor_total is not None else 0.0,
            "status": self.status,
            "destino_id": self.destino_id,
            "usuario_id": self.usuario_id
        }
