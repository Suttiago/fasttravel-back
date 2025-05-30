from repository.DependenteRepository import DependenteRepository
from models.Dependentes import Dependentes

class DependenteService:
    def __init__(self,db):
        self.repo = DependenteRepository(db)
        
        
    def salvar_dependente(self,dependente : Dependentes):
        return self.repo.criar_dependente(dependente)
        