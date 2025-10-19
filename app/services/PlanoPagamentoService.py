from sqlalchemy.orm import Session
from repository.PlanoPagamentoRepository import PlanoPagamentoRepository
from models.PlanoPagamento import PlanoPagamento

class PlanoPagamentoService:

    def __init__(self, db: Session):
        self.db = db
        self.repo = PlanoPagamentoRepository(db)

    def criar_novo_plano(self, plano: PlanoPagamento) -> PlanoPagamento:
        return self.repo.criar_novo_plano(plano)

    def listar_todos_planos(self) -> list[PlanoPagamento]:
        return self.repo.listar_todos()

    def buscar_plano_por_id(self, plano_id: int) -> PlanoPagamento | None:
        return self.repo.buscar_por_id(plano_id)

    def buscar_plano_por_conta_id(self, conta_pagar_id: int) -> PlanoPagamento | None:
        return self.repo.buscar_por_conta_id(conta_pagar_id)

    def atualizar_plano(self, plano_id: int, dados: dict) -> PlanoPagamento | None:
        return self.repo.editar_plano(plano_id, dados)

    def remover_plano(self, plano_id: int) -> bool:
        return self.repo.excluir_plano(plano_id)
