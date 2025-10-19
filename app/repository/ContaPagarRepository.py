
from models.ContaPagar import ContasPagar # Importe seu modelo
from sqlalchemy.orm import Session

class ContaPagarRepository:
    
    def __init__(self, db: Session):
        self.db = db

    def criar_conta(self, conta: ContasPagar) -> ContasPagar:
        self.db.add(conta)
        self.db.commit()
        self.db.refresh(conta)
        return conta

    def listar_contas(self) -> list[ContasPagar]:
        """Retorna todas as contas a receber do banco de dados."""
        return self.db.query(ContasPagar).all()

    def buscar_conta_por_id(self, conta_id: int) -> ContasPagar | None:
        """Busca uma conta a receber específica pelo seu ID."""
        return self.db.query(ContasPagar).filter(ContasPagar.id == conta_id).first()

    def editar_conta(self, conta_id: int, dados_atualizados: dict) -> ContasPagar | None:
        """Atualiza os dados de uma conta a receber existente."""
        conta = self.buscar_conta_por_id(conta_id)
        if conta:
            # Itera sobre o dicionário de dados e atualiza os atributos do objeto
            for chave, valor in dados_atualizados.items():
                setattr(conta, chave, valor)
            
            self.db.commit()
            self.db.refresh(conta)
        return conta

    def excluir_conta(self, conta_id: int) -> ContasPagar | None:
        """Exclui uma conta a receber do banco de dados."""
        conta = self.buscar_conta_por_id(conta_id)
        if conta:
            self.db.delete(conta)
            self.db.commit()
        return conta
    
    def atualizar_status(self, conta_id: int, novo_status: str) -> ContasPagar | None:
        """
        Busca uma conta pelo ID e atualiza apenas o seu status.
        """
        conta = self.buscar_conta_por_id(conta_id)
        if conta:
            conta.status = novo_status
            self.db.commit()
            self.db.refresh(conta)
        return conta