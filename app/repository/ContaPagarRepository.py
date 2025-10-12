
from models.ContaPagar import ContaPagar # Importe seu modelo
from sqlalchemy.orm import Session

class ContaPagarRepository:
    
    def __init__(self, db: Session):
        self.db = db

    def criar_conta(self, conta: ContaPagar) -> ContaPagar:
        self.db.add(conta)
        self.db.commit()
        self.db.refresh(conta)
        return conta

    def listar_contas(self) -> list[ContaPagar]:
        """Retorna todas as contas a receber do banco de dados."""
        return self.db.query(ContaPagar).all()

    def buscar_conta_por_id(self, conta_id: int) -> ContaPagar | None:
        """Busca uma conta a receber específica pelo seu ID."""
        return self.db.query(ContaPagar).filter(ContaPagar.id == conta_id).first()

    def editar_conta(self, conta_id: int, dados_atualizados: dict) -> ContaPagar | None:
        """Atualiza os dados de uma conta a receber existente."""
        conta = self.buscar_conta_por_id(conta_id)
        if conta:
            # Itera sobre o dicionário de dados e atualiza os atributos do objeto
            for chave, valor in dados_atualizados.items():
                setattr(conta, chave, valor)
            
            self.db.commit()
            self.db.refresh(conta)
        return conta

    def excluir_conta(self, conta_id: int) -> ContaPagar | None:
        """Exclui uma conta a receber do banco de dados."""
        conta = self.buscar_conta_por_id(conta_id)
        if conta:
            self.db.delete(conta)
            self.db.commit()
        return conta