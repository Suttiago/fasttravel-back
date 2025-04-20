from database.db import Database 
from dotenv import load_dotenv
import os



#conexao banco
load_dotenv()

banco = Database(
    usuario = os.getenv('DB_USER'),
    senha = os.getenv('DB_PASSWORD'),
    host = os.getenv('DB_HOST'),
    porta = os.getenv('DB_PORT'),
    nome_banco = os.getenv('DB_BAME')
)
banco.conectar_banco()



