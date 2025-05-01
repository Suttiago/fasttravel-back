from datetime import date
from models.orcamento import Orcamento
from controllers.orcamento_controller import Orcamento_controller
from controllers.user_controller import User_controller
from models.user import Usuario

# Criar um orçamento
orcamento = Orcamento(
    destino="Paris",
    check_in=date(2025, 6, 1),
    check_out=date(2025, 6, 10),
    adultos=2,
    criancas=1
)

# Inserir o orçamento no banco
controller = Orcamento_controller()
controller.inserir_orcamento(orcamento)

usuario = Usuario(
    nome ='tiago',
    cpf = '800.381.809-52',
    renda_mensal= 2.300,
    trabalho= 'Assistente de TI',
    data_nascimento= date(2006,9,16)
)
controller = User_controller()
controller.inserir_usuario(usuario)