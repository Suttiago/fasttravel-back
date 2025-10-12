from models.ContaPagar import ContaPagar
from repository.ContaPagarRepository import ContaPagarRepository
from sqlalchemy.orm import Session
from datetime import timedelta

class ContaPagarService:
    """
    Esta classe de serviço contém a lógica de negócio para
    gerenciar as Contas a Receber.
    """
    def __init__(self, db: Session):
        self.db = db
        self.repo = ContaPagarRepository(db)

    def criar_nova_conta(self, conta: ContaPagar, parcelas: int = 1, intervalo_dias: int = 30) -> list[ContaPagar]:
        """
        Salva uma nova conta a receber no banco de dados.
        Delega a criação para o repositório.
        """
        contas_criadas = []
        
        if parcelas <= 1:
            nova_conta = self.repo.criar_conta(conta)
            contas_criadas.append(nova_conta)
        else:
            valor_parcela = round(conta.valor / parcelas, 2)
            
            for i in range(parcelas):
                nova_parcela = ContaPagar(
                    valor=valor_parcela,
                    dt_vencimento=conta.dt_vencimento + timedelta(days=i * intervalo_dias),
                    metodo_pagamento = conta.metodo_pagamento,
                    status="Pendente",
                    n_parcelas = conta.n_parcelas,
                    orcamento_id=conta.orcamento_id
                )
                conta_criada = self.repo.criar_conta(nova_parcela)
                contas_criadas.append(conta_criada)
            
        return contas_criadas

    def listar_todas_contas(self) -> list[ContaPagar]:
        """
        Lista todas as contas a receber existentes.
        Delega a listagem para o repositório.
        """
        return self.repo.listar_contas()

    def buscar_conta_por_id(self, conta_id: int) -> ContaPagar | None:
        """
        Busca uma conta específica pelo seu ID.
        Delega a busca para o repositório.
        """
        return self.repo.buscar_conta_por_id(conta_id)

    def listar_contas_por_orcamento(self, orcamento_id: int) -> list[ContaPagar]:
        """
        Busca todas as contas a receber associadas a um orçamento específico.
        """
        return self.db.query(ContaPagar).filter(ContaPagar.orcamento_id == orcamento_id).all()

    def atualizar_conta(self, conta_id: int, dados: dict) -> ContaPagar | None:
        """
        Atualiza os dados de uma conta a receber.
        Delega a atualização para o repositório.
        """
        return self.repo.editar_conta(conta_id, dados)

    def atualizar_status_pagamento(self, conta_id: int, novo_status: str) -> ContaPagar | None:
        """
        Atualiza apenas o status de uma conta a receber (ex: "Pendente" para "Pago").
        """
        conta_db = self.repo.buscar_conta_por_id(conta_id)
        if conta_db:
            conta_db.status = novo_status
            self.db.commit()
            self.db.refresh(conta_db)
            return conta_db
        return None

    def remover_conta(self, conta_id: int) -> ContaPagar | None:
        """
        Exclui uma conta a receber do sistema.
        Delega a exclusão para o repositório.
        """
        return self.repo.excluir_conta(conta_id)