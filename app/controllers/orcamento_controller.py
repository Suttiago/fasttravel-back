from database.conn import  banco
from models.orcamento import Orcamento
 
class Orcamento_controller:
    
    def inserir_orcamento(self, orcamento: Orcamento):
        query= '''Insert into ORCAMENTOS (DESTINO, CHECK_IN, CHECK_OUT, ADULTOS, CRIANCAS)
            VALUES(%s,%s,%s,%s,%s) '''
        parametros = (
            orcamento.destino,
            orcamento.check_in,
            orcamento.check_out,
            orcamento.adultos,
            orcamento.criancas
        )
        banco.executar_query(query,parametros)
        
   # def editar_orcamento():
   #     query = 
   #     
   #     parametros
   #     
   #     
   # def excluir_orcamento():
   #     
   #     
   # def ler_orcamento():
   #     