from models.InfoFlights import Passagem
from repository.InfoFlightsRepository import PassagemRepository
from dotenv import load_dotenv
import json
import os
from serpapi.google_search import GoogleSearch

class PassagemService:
    load_dotenv()
    def __init__(self, db):
        self.db = db
        self.repo = PassagemRepository(db)

    def salvar_passagem(self, passagem: Passagem):
        return self.repo.criar_passagem(passagem)
    
    def listar_passagens(self):
        return self.repo.listar_passagens()

    def listar_passagens_por_destino(self, destino_id):
        return self.db.query(Passagem).filter_by(destino_id=destino_id).all()

    def editar_passagem(self, passagem_id, origem, destino, preco, disponibilidade):
        passagem_db = self.db.query(Passagem).filter_by(id=passagem_id).first()
        if passagem_db:
            passagem_db.origem = origem
            passagem_db.destino = destino
            passagem_db.preco = preco
            passagem_db.disponibilidade = disponibilidade
            self.db.commit()
            self.db.refresh(passagem_db)
            return passagem_db
        return None
    
    def excluir_passagem(self, passagem_id):
        return self.repo.excluir_passagem(passagem_id)

    def buscar_passagem(self,codigo_iat,check_in,check_out):
        params = {
            "engine": "google_flights",
            "departure_id": "GRU",  
            "arrival_id": codigo_iat,    
            "outbound_date": check_in,
            "return_date": check_out, 
            "currency": "BRL",
            "gl": "br",
            "hl": "pt-br",
            "api_key": os.getenv("HOTEL_API_KEY")
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        return results