from sqlalchemy.orm import Session
from models.PlanoPagamento import PlanoPagamento
from repository.ContaPagarRepository import ContaPagarRepository
from repository.OrcamentoRepository import OrcamentoRepository
class PlanoPagamentoRepository:
    """
    Este repositório gerencia as operações de banco de dados
    para o modelo PlanoPagamento.
    """
    def __init__(self, db: Session):
        self.db = db
        self.conta_pagar_repo = ContaPagarRepository(db)
        self.orcamento_repo = OrcamentoRepository(db)
    def criar_novo_plano(self, plano: PlanoPagamento) -> PlanoPagamento:
        """
        Cria um novo plano de pagamento e, em caso de sucesso,
        atualiza o status da ContaPagar associada para 'Pago'.
        """
        self.db.add(plano)
        self.db.commit()
        self.db.refresh(plano)
        plano_criado = plano 

        if plano_criado:
            conta_id = plano_criado.contas_pagar_id
            conta_paga = self.conta_pagar_repo.atualizar_status(conta_id, "Pago")

            if conta_paga:
                orcamento_id = conta_paga.orcamento_id
                self.orcamento_repo.atualizar_status(orcamento_id, "Pagamento Feito")

        return plano_criado

    def listar_todos(self) -> list[PlanoPagamento]:
        """Retorna todos os planos de pagamento do banco de dados."""
        return self.db.query(PlanoPagamento).all()

    def buscar_por_id(self, plano_id: int) -> PlanoPagamento | None:
        """Busca um plano de pagamento específico pelo seu ID."""
        return self.db.query(PlanoPagamento).filter_by(id=plano_id).first()
    
    def buscar_por_conta_id(self, conta_pagar_id: int) -> PlanoPagamento | None:
        """Busca um plano de pagamento pela ID da conta a pagar associada."""
        return self.db.query(PlanoPagamento).filter_by(conta_pagar_id=conta_pagar_id).first()

    def editar_plano(self, plano_id: int, dados_atualizados: dict) -> PlanoPagamento | None:
        """Atualiza os dados de um plano de pagamento existente."""
        plano = self.buscar_por_id(plano_id)
        if plano:
            for chave, valor in dados_atualizados.items():
                # Garante que não se tente alterar o ID
                if hasattr(plano, chave) and chave != 'id':
                    setattr(plano, chave, valor)
            self.db.commit()
            self.db.refresh(plano)
        return plano

    def excluir_plano(self, plano_id: int) -> bool:
        """Exclui um plano de pagamento do banco de dados."""
        plano = self.buscar_por_id(plano_id)
        if not plano:
            return False
        
        self.db.delete(plano)
        self.db.commit()
        return True
