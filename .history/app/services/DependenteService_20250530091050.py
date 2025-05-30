from repository.DependenteRepository import DependenteRepository
from models.Dependentes import Dependentes

class DependenteService:
    def __init__(self,db):
        self.repo = DependenteRepository(db)
        
        
    def salvar_dependente(self,dependente : Dependentes):
        return self.repo.criar_dependente(dependente)
    
    def listar_dependentes(self,dependente : Dependentes):
        return self.repo.listar_dependente(dependente)
    
    def editar_dependente(self, dependente : Dependentes):
        return self.repo.editar_dependente(dependente)
    
    def excluir_dependente(self, dependente: Dependentes):
        return self.repo.excluir_dependente(dependente)