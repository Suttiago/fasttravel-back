from repository.DependenteRepository import DependenteRepository
from models.Dependentes import Dependentes

class DependenteService:
    def __init__(self,db):
        self.db = DependenteRepository(db)
        
        
    def salvar_dependente(dependente : Dep)
        