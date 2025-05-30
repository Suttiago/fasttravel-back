from database.db import Base, engine
from models.Usuario import Usuario
from models.PlanoPagamento import PlanoPagamento
from models.ContaReceber import ContaReceber
from models.Dependentes import Dependentes
from models.Orcamento import Orcamento
from models.Pessoa import Pessoa
Base.metadata.create_all(bind=engine)