from models.InfoHotels import Hotels

class HotelsRepository:
    def __init__(self, db):
        self.db = db

    def criar_hotel(self, hotel: Hotels):
        self.db.add(hotel)
        self.db.commit()
        self.db.refresh(hotel)
        return hotel

    def listar_hoteis(self):
        return self.db.query(Hotels).all()

    def buscar_por_id(self, hotel_id: int):
        return self.db.query(Hotels).filter_by(id=hotel_id).first()

    def editar_hotel(self, hotel: Hotels):
        hotel_db = self.db.query(Hotels).filter_by(id=hotel.id).first()
        if hotel_db:
            hotel_db.hotel = hotel.hotel
            hotel_db.hotel_classification = hotel.hotel_classification
            hotel_db.hotel_description = hotel.hotel_description
            hotel_db.hotel_price = hotel.hotel_price
            hotel_db.destino_id = hotel.destino_id

            self.db.commit()
            self.db.refresh(hotel_db)
            return hotel_db
        return None

    def excluir_hotel(self, hotel_id: int):
        hotel_db = self.db.query(Hotels).filter_by(id=hotel_id).first()
        if hotel_db:
            self.db.delete(hotel_db)
            self.db.commit()
            return True
        return False

    def buscar_por_nome(self, nome: str):
        return self.db.query(Hotels).filter_by(hotel=nome).first()
