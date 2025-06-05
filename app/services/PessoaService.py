from repository.PessoaRepository import PessoaRepository

class PessoaService:
    def __init__(self, db):
        self.repo = PessoaRepository(db)

    def criar_pessoa(self, pessoa):
        return self.repo.criar_pessoa(pessoa)

    def listar_pessoas(self):
        return self.repo.listar_pessoas()

    def buscar_por_id(self, pessoa_id):
        return self.repo.buscar_por_id(pessoa_id)

    def listar_dependentes(self, responsavel_id):
        return self.repo.listar_dependentes(responsavel_id)