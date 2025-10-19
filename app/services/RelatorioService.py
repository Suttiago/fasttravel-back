from sqlalchemy.orm import Session
from models.Orcamento import Orcamento
from models.ContaPagar import ContasPagar
from models.Destino import Destino
import pandas as pd
from weasyprint import HTML
import base64

class RelatorioService:
    def __init__(self, db: Session):
        self.db = db

    def gerar_relatorio_usuario(self, usuario_id: int) -> dict:
        """
        Busca todos os dados financeiros de um usuário, incluindo o nome do destino,
        e compila um relatório em formato JSON.
        """
        resultados = (
            self.db.query(Orcamento, Destino)
            .join(Destino, Orcamento.destino_id == Destino.id)
            .filter(Orcamento.usuario_id == usuario_id)
            .all()
        )

        if not resultados:
            return {
                "resumo": { "total_orcamentos": 0, "valor_total_geral": 0, "total_pago": 0, "total_pendente": 0 },
                "orcamentos_detalhados": []
            }
            
        orcamentos = [res[0] for res in resultados]
        orcamento_ids = [o.id for o in orcamentos]
        contas = self.db.query(ContasPagar).filter(ContasPagar.orcamento_id.in_(orcamento_ids)).all()

        valor_total_geral = sum(o.valor_total for o in orcamentos)
        total_pago = sum(c.valor for c in contas if c.status.lower() == 'pago')
        total_pendente = sum(c.valor for c in contas if c.status.lower() == 'pendente')
        
        orcamentos_detalhados = []
        for orcamento, destino in resultados:
            orc_dict = orcamento.to_dict()
            orc_dict['nome_destino'] = destino.destino
            orcamentos_detalhados.append(orc_dict)

        relatorio = {
            "resumo": {
                "total_orcamentos": len(orcamentos),
                "valor_total_geral": float(valor_total_geral),
                "total_pago": float(total_pago),
                "total_pendente": float(total_pendente),
            },
            "orcamentos_detalhados": orcamentos_detalhados
        }
        return relatorio


    def gerar_relatorio_pdf_usuario(self, usuario_id: int) -> dict:
        """
        Gera um relatório financeiro em PDF para o usuário, codificado em Base64,
        e retorna num formato serializável para JSON.
        """
        dados_json = self.gerar_relatorio_usuario(usuario_id)
        resumo = dados_json['resumo']
        detalhes = dados_json['orcamentos_detalhados']

        if not detalhes:
            html_string = "<html><body><h1>Relatório Financeiro</h1><p>Nenhum dado encontrado.</p></body></html>"
            pdf_bytes = HTML(string=html_string).write_pdf()
            base64_encoded_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
            return {"pdf_base64": base64_encoded_pdf}

        # Renomeia as colunas do resumo para exibição
        df_resumo = pd.DataFrame.from_records([resumo])
        df_resumo.rename(columns={
            'total_orcamentos': 'Total de Orçamentos',
            'valor_total_geral': 'Valor Total Geral',
            'total_pago': 'Total Pago',
            'total_pendente': 'Total Pendente'
        }, inplace=True)

        df_detalhes = pd.DataFrame.from_records(detalhes)
        df_detalhes.rename(columns={
            'id': 'ID', 'nome_destino': 'Destino', 'valor_total': 'Valor Total',
            'status': 'Status', 'valor_passagens': 'Passagens', 'valor_hoteis': 'Hotéis'
        }, inplace=True)

        # Define as colunas a serem exibidas na tabela de detalhes, sem o 'ID'
        colunas_para_exibir = ['Destino', 'Passagens', 'Hotéis', 'Valor Total', 'Status']
        df_detalhes_final = df_detalhes[colunas_para_exibir]

        # Formata as colunas de moeda
        for col in ['Valor Total Geral', 'Total Pago', 'Total Pendente']:
            df_resumo[col] = df_resumo[col].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        
        for col in ['Valor Total', 'Passagens', 'Hotéis']:
            if col in df_detalhes_final.columns:
                df_detalhes_final[col] = df_detalhes_final[col].apply(lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

        # Gera a string HTML com o CSS corrigido
        html_string = f"""
        <html>
            <head>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <style>
                    body {{ font-family: sans-serif; }}
                    h1, h2 {{ text-align: center; color: #333; }}
                    .table {{ 
                        margin-top: 20px; 
                        font-size: 10pt; 
                        table-layout: fixed; 
                        width: 100%; 
                        border-collapse: collapse;
                    }}
                    .table th, .table td {{
                        text-align: center; /* Alinha números à direita por padrão */
                        vertical-align: middle;
                        padding: 8px;
                    }}
                    .table th {{
                        text-align: center; /* Centraliza cabeçalhos */
                    }}
                    .detalhes-table td:nth-child(1), /* Coluna Destino */
                    .detalhes-table td:nth-child(5)  /* Coluna Status */
                    {{
                        text-align: center; /* Alinha texto à esquerda */
                    }}
                    .resumo-table {{ width: 90%; margin-left: auto; margin-right: auto; }}
                    
                    /* --- AJUSTE DE LARGURA DAS COLUNAS (Resumo) --- */
                    .resumo-table th:nth-child(1) {{ width: 17%; }}  /* Total de Orçamentos */
                    .resumo-table th:nth-child(2) {{ width: 30%; }}  /* Valor Total Geral */
                    .resumo-table th:nth-child(3) {{ width: 25%; }}  /* Total Pago */
                    .resumo-table th:nth-child(4) {{ width: 25%; }}  /* Total Pendente */

                    /* --- AJUSTE DE LARGURA DAS COLUNAS (Detalhes) --- */
                    .detalhes-table th:nth-child(1) {{ width: 30%; }}  /* Destino */
                    .detalhes-table th:nth-child(2),
                    .detalhes-table th:nth-child(3),
                    .detalhes-table th:nth-child(4) {{ width: 17%; }}  /* Valores */
                    .detalhes-table th:nth-child(5) {{ width: 19%; }}  /* Status */
                </style>
            </head>
            <body>
                <h1>Relatório Financeiro</h1>
                <h2>Resumo Geral</h2>
                {df_resumo.to_html(classes='table table-bordered resumo-table', index=False)}
                <h2 style="margin-top: 40px;">Detalhes dos Orçamentos</h2>
                {df_detalhes_final.to_html(classes='table table-striped detalhes-table', index=False)}
            </body>
        </html>
        """

        pdf_bytes = HTML(string=html_string).write_pdf()
        base64_encoded_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
        return  base64_encoded_pdf

    def gerar_relatorio_destinos_pdf_usuario(self, usuario_id: int) -> dict:
        """
        Gera um relatório de destinos em PDF para o usuário, codificado em Base64.
        """
        destinos = self.db.query(Destino).filter_by(usuario_id=usuario_id).order_by(Destino.check_in).all()

        if not destinos:
            html_string = "<html><body><h1>Relatório de Destinos</h1><p>Nenhum destino encontrado.</p></body></html>"
            pdf_bytes = HTML(string=html_string).write_pdf()
            base64_encoded_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
            return {"pdf_base64": base64_encoded_pdf}

        dados_para_df = []
        for d in destinos:
            dados_para_df.append({
                'Destino': d.destino,
                'Check-in': d.check_in.strftime('%d/%m/%Y') if d.check_in else '-',
                'Check-out': d.check_out.strftime('%d/%m/%Y') if d.check_out else '-',
                'Viajantes': (d.adultos or 0) + (d.criancas or 0),
                'Status': d.status
            })

        df_detalhes = pd.DataFrame.from_records(dados_para_df)

        html_string = f"""
        <html>
            <head>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <style>
                    body {{ font-family: sans-serif; }}
                    h1 {{ text-align: center; color: #333; margin-bottom: 30px; }}
                    .table {{ font-size: 10pt; width: 100%; }}
                    .table th {{ text-align: center; background-color: #f2f2f2; }}
                    .table td {{ text-align: center; padding: 8px; }}
                    .table td:first-child {{ text-align: left; }} /* Alinha nome do destino à esquerda */
                </style>
            </head>
            <body>
                <h1>Relatório de Destinos</h1>
                {df_detalhes.to_html(classes='table table-striped', index=False, justify='center')}
            </body>
        </html>
        """

        pdf_bytes = HTML(string=html_string).write_pdf()
        base64_encoded_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
        
        return base64_encoded_pdf

