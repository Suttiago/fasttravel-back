from services.InfoFlightsService import PassagemService
from services.InfoHotelsService import HotelService
from repository.OrcamentoRepository import OrcamentoRepository
from models.Orcamento import Orcamento

class OrcamentoService:
    def __init__(self, db):
        self.db = db
        self.repo = OrcamentoRepository(db)
        self.passagem_service = PassagemService(db)
        self.hotel_service = HotelService(db)

    def gerar_orcamento(self, destino_id: int):
        # buscar passagens e hoteis para o destino
        passagens = self.passagem_service.listar_passagens_por_destino(destino_id)
        hoteis = self.hotel_service.listar_hoteis_por_destino(destino_id)

        total_passagens = sum([p.preco_passagem or 0 for p in passagens])
        total_hoteis = sum([h.hotel_price or 0 for h in hoteis])
        valor_total = total_passagens + total_hoteis

        orcamento = Orcamento(
            valor_passagens=total_passagens,
            valor_hoteis=total_hoteis,
            valor_total=valor_total,
            status='Pagamento Pendente',
            destino_id=destino_id
        )

        return self.repo.criar(orcamento)

    def listar_orcamentos(self):
        return self.repo.listar_tudo()

    def excluir_orcamento(self, orcamento_id: int):
        return self.repo.excluir(orcamento_id)

    def editar_orcamento(self, orcamento_id: int, status: str):
        return self.repo.atualizar_status(orcamento_id, status)
    
    def listar_orcamento_dest(self,destino_id):
        # retorna todos os orçamentos relacionados ao destino_id informado
        return self.db.query(Orcamento).filter_by(destino_id=destino_id).all()
