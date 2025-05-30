from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from database.db import Base


class Pessoa():
    __tablename__ = 'PESSOAS'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    sexo = Column(String)
    profissao = Column(String)
    renda = Column(Float)
    
    type = Column(String)
    __mapper_args__={
        'polymorphic_identity': 'pessoa',
        'polymorphic_on': type
    }
