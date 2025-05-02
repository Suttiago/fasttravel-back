from datetime import date
from models.orcamento import Orcamento
from controllers.orcamento_controller import Orcamento_controller
from controllers.user_controller import User_controller
from models.user import Usuario

usuario = Usuario(
    nome ='izzy',
    cpf = '071.081.11-24',
    renda_mensal= 2.300,
    trabalho= 'Estagiária neddiji',
    data_nascimento= date(2005,10,5)
)
controller = User_controller()
controller.inserir_usuario(usuario)