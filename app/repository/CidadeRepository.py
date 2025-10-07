from models.Cidades import Cidades


class CidadeRepository:
    def __init__(self, db):
        self.db = db

    def criar_cidade(self, cidade: Cidades):
        self.db.add(cidade)
        self.db.commit()
        self.db.refresh(cidade)
        return cidade

    def listar_tudo(self):
        return self.db.query(Cidades).all()

    def buscar_por_id(self, cidade_id: int):
        return self.db.query(Cidades).filter_by(id=cidade_id).first()

    def buscar_por_codigo_iat(self, codigo_iat: str):
        return self.db.query(Cidades).filter_by(codigo_iat=codigo_iat).first()

    def editar_cidade(self, cidade: Cidades):
        cidade_db = self.db.query(Cidades).filter_by(id=cidade.id).first()
        if cidade_db:
            cidade_db.nome = cidade.nome
            cidade_db.codigo_iat = cidade.codigo_iat
            self.db.commit()
            self.db.refresh(cidade_db)
            return cidade_db
        return None

    def excluir_cidade(self, cidade_id: int):
        cidade_db = self.db.query(Cidades).filter_by(id=cidade_id).first()
        if cidade_db:
            self.db.delete(cidade_db)
            self.db.commit()
            return True
        return False
