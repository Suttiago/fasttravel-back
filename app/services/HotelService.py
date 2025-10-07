from dotenv import load_dotenv
import os
import json
from serpapi.google_search import GoogleSearch

load_dotenv()
api_key = os.getenv("HOTEL_API_KEY") # Certifique-se que o nome da variável no .env é SERPAPI_API_KEY

if not api_key:
    raise ValueError("A chave da API (SERPAPI_API_KEY) não foi encontrada no arquivo .env")

# --- ÚNICA ALTERAÇÃO ESTÁ AQUI ---
# Trocamos a rota por uma rota comercial válida e popular para garantir resultados.
params = {
    "engine": "google_flights",
    "departure_id": "GRU",  # Aeroporto de Guarulhos, São Paulo
    "arrival_id": "MIA",    # Aeroporto de Miami, EUA
    "outbound_date": "2025-10-03",
    "return_date": "2025-10-10", # Aumentei um pouco a data de volta para ser mais realista
    "currency": "BRL",
    "gl": "br",
    "hl": "pt-br",
    "api_key": api_key
}

print(f"Buscando voos de {params['departure_id']} para {params['arrival_id']}...")

search = GoogleSearch(params)
results = search.get_dict()

# Agora, este JSON terá todas as informações que você espera
print("\n--- JSON Completo Retornado pela API ---")
print(json.dumps(results, indent=2, ensure_ascii=False))