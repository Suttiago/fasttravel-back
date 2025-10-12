from models.Orcamento import Orcamento

class OrcamentoRepository:
	def __init__(self, db):
		self.db = db

	def criar(self, orcamento: Orcamento):
		self.db.add(orcamento)
		self.db.commit()
		self.db.refresh(orcamento)
		return orcamento

	def listar_tudo(self):
		return self.db.query(Orcamento).all()

	def buscar_por_id(self, orcamento_id: int):
		return self.db.query(Orcamento).filter_by(id=orcamento_id).first()

	def excluir(self, orcamento_id: int):
		o = self.buscar_por_id(orcamento_id)
		if not o:
			return False
		self.db.delete(o)
		self.db.commit()
		return True

	def atualizar_status(self, orcamento_id: int, status: str):
		o = self.buscar_por_id(orcamento_id)
		if not o:
			return None
		o.status = status
		self.db.commit()
		self.db.refresh(o)
		return o

