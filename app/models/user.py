from pydantic import BaseModel
from datetime import date
from models.orcamento import Orcamento

class Usuario(BaseModel):
    nome : str 
    cpf : str
    email : str
    senha : str
    renda_mensal : float
    trabalho : str
    data_nascimento : date
    