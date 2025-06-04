from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base


class Pessoa(Base):
    __tablename__ = 'PESSOAS'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    sexo = Column(String)
    profissao = Column(String)
    renda = Column(Float)

   
    responsavel_id = Column(Integer, ForeignKey('PESSOAS.id'), nullable=True)

   
    responsavel = relationship(
        "Pessoa",                      
        remote_side=[id],              
        back_populates="dependentes"  
    )


    dependentes = relationship(
        "Pessoa",
        back_populates="responsavel",
        cascade="all, delete-orphan"
    )

    type = Column(String)
    __mapper_args__ = {
        'polymorphic_identity': 'pessoa',
        'polymorphic_on': type
    }

