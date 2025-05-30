from models.Pessoa import Pessoa
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Dependentes(Pessoa):
    __tablename__ = 'DEPENDENTES'

    id = Column(Integer, ForeignKey('PESSOAS.id'), primary_key=True)
    usuario_id = Column(Integer, ForeignKey('USUARIOS.id'), nullable=False)

    usuario = relationship("Usuario", back_populates="dependentes",
    foreign_keys=[usuario_id])

    __mapper_args__ = {
        'polymorphic_identity': 'dependente',
    }