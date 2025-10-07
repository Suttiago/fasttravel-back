from models.Cidades import Cidades
from repository.CidadeRepository import CidadeRepository


class CidadeService:
    def __init__(self, db):
        self.db = db
        self.repo = CidadeRepository(db)

    def salvar_cidade(self, cidade: Cidades):
        return self.repo.criar_cidade(cidade)

    def listar_todas(self):
        return self.repo.listar_tudo()

    def buscar_por_id(self, cidade_id: int):
        return self.repo.buscar_por_id(cidade_id)

    def buscar_por_codigo_iat(self, codigo_iat: str):
        return self.repo.buscar_por_codigo_iat(codigo_iat)

    def buscar_por_nome(self, termo: str):
        query = self.db.query(Cidades).filter(
            Cidades.nome.ilike(f"%{termo}%")
        )
        return query.order_by(Cidades.nome).limit(10).all()
        
    def editar_cidade(self, cidade: Cidades):
        return self.repo.editar_cidade(cidade)

    def excluir_cidade(self, cidade_id: int):
        return self.repo.excluir_cidade(cidade_id)
