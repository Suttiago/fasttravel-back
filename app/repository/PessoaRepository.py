from models.Pessoa import Pessoa

class PessoaRepository:
    def __init__(self, db):
        self.db = db

    def criar_pessoas(self, pessoa: Pessoa):
        self.db.add(pessoa)
        self.db.commit()
        self.db.refresh(pessoa)
        return pessoa

    def listar_pessoas(self):
        return self.db.query(Pessoa).all()

    def editar_pessoas(self, pessoa:Pessoa):
        pessoa_db= self.db.query(Pessoa).filter_by(id=pessoa.id)
        if pessoa_db:
            pessoa_db.nome  = pessoa.nome
            pessoa_db.data_nascimento = pessoa.data_nascimento
            pessoa_db.sexo = pessoa.sexo
            pessoa_db.profissao = pessoa.profissao
            pessoa_db.renda = pessoa.renda
            self.db.commit()
            self.db.refresh(pessoa_db)
            return pessoa_db
        
    def buscar_por_id(self, pessoa_id):
        return self.db.query(Pessoa).filter_by(id=pessoa_id).first()

    def listar_dependentes(self, responsavel_id):
        return self.db.query(Pessoa).filter_by(responsavel_id=responsavel_id).all()
    
    def excluir_dependentes(self, dependente_id):
        dependente = self.db.query(Pessoa).filter_by(id=dependente_id).first()
        if dependente:
            self.db.delete(dependente)
            self.db.commit()
