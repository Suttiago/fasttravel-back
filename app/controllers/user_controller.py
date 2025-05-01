from database.conn import  banco
from models.user import Usuario
 
class User_controller:
    
    def inserir_usuario(self, usuario: Usuario):
        query= '''Insert into usuarios (NOME, CPF, RENDA_MENSAL, TRABALHO, DATA_NASCIMENTO)
            VALUES(%s,%s,%s,%s,%s)'''
        parametros = (
            usuario.nome,
            usuario.cpf,
            usuario.renda_mensal,
            usuario.trabalho,
            usuario.data_nascimento
        )
        banco.executar_query(query,parametros)
        
    #def editar_orcamento():
    #    query = 
    #    
    #    parametros
    #    
    #    
    #def excluir_orcamento():
    #    
    #    
    #def ler_orcamento():
    #    