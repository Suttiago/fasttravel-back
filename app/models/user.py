
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
    

