from models.Pessoa import Pessoa

class PessoaRepository:
    def __init__(self, db):
        self.db = db

    def criar_pessoa(self, pessoa: Pessoa):
        self.db.add(pessoa)
        self.db.commit()
        self.db.refresh(pessoa)
        return pessoa

    def listar_pessoas(self):
        return self.db.query(Pessoa).all()

    def buscar_por_id(self, pessoa_id):
        return self.db.query(Pessoa).filter_by(id=pessoa_id).first()

    def listar_dependentes(self, responsavel_id):
        return self.db.query(Pessoa).filter_by(responsavel_id=responsavel_id).all()