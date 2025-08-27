from repository.PessoaRepository import PessoaRepository
from models.Pessoa import Pessoa

class PessoaService:
    def __init__(self, db):
        self.db = db
        self.repo = PessoaRepository(db)

    def criar_pessoa(self, pessoa):
        return self.repo.criar_pessoas(pessoa)

    def listar_pessoas(self):
        return self.repo.listar_pessoas()

    def buscar_por_id(self, pessoa_id):
        return self.repo.buscar_por_id(pessoa_id)

    def listar_dependentes(self, responsavel_id):
        return self.repo.listar_dependentes(responsavel_id)
    
    def excluir_dependentes(self, dependente_id):
        return self.repo.excluir_dependentes(dependente_id)
    
    def editar_dependentes(self, dependente_id,nome,cpf,data_nascimento):
        dependente_db = self.db.query(Pessoa).filter_by(id=dependente_id).first()
        if dependente_db:
            dependente_db.nome = nome
            dependente_db.cpf = cpf
            dependente_db.data_nascimento = data_nascimento
            self.db.commit()
            self.db.refresh(dependente_db)
            return dependente_db
        return None
    
    