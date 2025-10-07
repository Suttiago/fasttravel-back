from database.db import Base, engine
from models.Usuario import Usuario
from models.PlanoPagamento import PlanoPagamento
from models.ContaReceber import ContaReceber
from models.Orcamento import Orcamento
from models.Pessoa import Pessoa
from models.InfoFlights import Passagem
from models.InfoHotels import Hotels
from models.Destino import Destino
from models.Cidades import Cidades

Base.metadata.create_all(bind=engine)