from database.conn import banco
from models.user import Usuario
 
class User_controller:
    
    def inserir_usuario(self, usuario: Usuario):
        query= '''Insert into USUARIOS (NOME, CPF, RENDA_MENSAL, TRABALHO, DATA_NASCIMENTO)
            VALUES(%s,%s,%s,%s,%s)'''
        parametros = (
            usuario.nome,
            usuario.cpf,
            usuario.renda_mensal,
            usuario.trabalho,
            usuario.data_nascimento
        )
        banco.executar_query(query,parametros)
        
    def editar_usuario(self,id: int, usuario: Usuario):
        query = '''UPDATE USUARIOS
        SET NOME = %s,
            CPF = %s,
            RENDA_MENSAL = %s,
            TRABALHO = %s,
            DATA_NASCIMENTO = %s
        WHERE ID = %s
        '''
        parametros = (
            usuario.nome,
            usuario.cpf,
            usuario.renda_mensal,
            usuario.trabalho,
            usuario.data_nascimento,
            id  
        )
        banco.executar_query(query,parametros)
            
    def excluir_usuario(self, id: int):
        query = '''DELETE FROM USUARIOS WHERE ID = %s'''
        parametros = (id)
        
        banco.executar_query(query,parametros)
    
    def ler_usuarios(self):
        query = '''SELECT * FROM USUARIOS'''
        banco.executar_query(query)
        