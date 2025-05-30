from models.Dependentes import Dependentes

class UserRepository:
    def __init__(self,db):
        self.db = db
    
    def criar_dependente(self, dependente : Dependentes):
        self.db.add(dependente)
        self.db.commit()
        self.db.refresh(dependente)
        return dependente

    def listar_dependente(self, dependente: Dependentes):
        self.db.query(dependente).filter_by(dependente.id).first()
        
    def editar_dependente(self, dependente:Dependentes):
        dependente_db = self.db.query(dependente).filter_by(id=dependente.id)
        if dependente_db:
            dependente_db.email = dependente.email
            dependente_db.senha = dependente.senha
            dependente_db.nome  = dependente.nome
            dependente_db.data_nascimento = dependente.data_nascimento
            dependente_db.sexo = dependente.sexo
            dependente_db.profissao = dependente.profissao
            dependente_db.renda = dependente.renda
            self.db.commit()
            self.db.refresh(dependente_db)
            return dependente_db
        
    
    def excluir_dependente(self, dependente: Dependentes):
        dependente_db = self.db.query(dependente).filter_by(id=dependente.id).first()
        if dependente_db:
            self.db.delete(dependente_db)
            self.db.commit()
            return True
        return False
