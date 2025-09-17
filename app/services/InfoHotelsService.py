from models.InfoHotels import Hotels
from repository.InfoHotelsRepository import HotelsRepository
from dotenv import load_dotenv
import json
import os
from serpapi.google_search import GoogleSearch



class HotelService:
    load_dotenv()
    hotel_api_key = os.getenv("API_KEY_HOTELS")
    def __init__(self, db):
        self.db = db
        self.repo = HotelsRepository(db)

    def salvar_hotel(self, hotel: Hotels):
        return self.repo.criar_hotel(hotel)
    
    def listar_hoteis(self):
        return self.repo.listar_hoteis()

    def listar_hoteis_por_destino(self, destino_id):
        return self.db.query(Hotels).filter_by(destino_id=destino_id).all()

    def editar_hotel(self, hotel_id, nome, preco, disponibilidade):
        hotel_db = self.db.query(Hotels).filter_by(id=hotel_id).first()
        if hotel_db:
            hotel_db.nome = nome
            hotel_db.preco = preco
            hotel_db.disponibilidade = disponibilidade
            self.db.commit()
            self.db.refresh(hotel_db)
            return hotel_db
        return None
    
    def excluir_hotel(self, hotel_id):
        return self.repo.excluir_hotel(hotel_id)

    def buscar_hoteis(self,destino,check_in,check_out,adultos,criancas):
        params = {
              "engine": "google_hotels",
              "q": destino,
              "check_in_date": check_in,
              "check_out_date": check_out,
              "adults": adultos,
              "children":criancas,
              "currency": "BRL",
              "gl": "br",
              "hl": "pt-br",
              "api_key": os.getenv("HOTEL_API_KEY")
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        return (json.dumps(results, indent=2, ensure_ascii=False))  
