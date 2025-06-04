from database.db import Base, engine
from models.Usuario import Usuario
from models.PlanoPagamento import PlanoPagamento
from models.ContaReceber import ContaReceber
from models.Orcamento import Orcamento
from models.Pessoa import Pessoa
from models.ContaReceber import ContaReceber
from models.InfoFlights import Passagens
from models.InfoHotels import Hotels
from models.Destino import Destino

Base.metadata.create_all(bind=engine)