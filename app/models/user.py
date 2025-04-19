<<<<<<< HEAD
from pydantic import BaseModel
from typing import List
from datetime import date
from orcamento import Orcamento

class Usuario(BaseModel):
    nome : str 
    cpf : str
    renda_mensal : float
    trabalho : str
    data_nascimento : date
    orcamentos: List[Orcamento] = []
    
    def novo_orcamento(self, destino: str, check_in: date, check_out: date, adultos: int, criancas: int):
        novo_orcamento = Orcamento(
            destino=destino,
            check_in=check_in,
            check_out=check_out,
            adultos=adultos,
            criancas=criancas
        )
        self.orcamentos.append(novo_orcamento)
        return novo_orcamento
    
    
=======
<<<<<<< HEAD
=======
 
class Usuario:
    def __init__(self, nome,cpf,renda_mensal,data_nascimento,trabalho):
        self.nome = nome
        self.cpf = cpf
        self.renda_mensal = renda_mensal
        self.trabalho = trabalho
        self.data_nascimento = data_nascimento
>>>>>>> a19e0e5bf3f4818a384e3bcfe11544e6c57355d2
>>>>>>> main
