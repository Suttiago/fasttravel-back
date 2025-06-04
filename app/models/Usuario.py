from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import  relationship
from models.Pessoa import Pessoa
class Usuario(Pessoa):
    __tablename__='USUARIOS'
    
    id = Column(Integer, ForeignKey('PESSOAS.id'), primary_key=True)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    
    orcamento = relationship("Orcamentos", back_populates='usuarios')
    destinos = relationship("Destino", back_populates="usuario")

    __mapper_args__ = {
        'polymorphic_identity': 'usuario',
    }
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "sexo": self.sexo,
            "profissao": self.profissao,
            "renda": self.renda,
            "data_nascimento": self.data_nascimento
            # Adicione outros campos se necessário
        }
    
