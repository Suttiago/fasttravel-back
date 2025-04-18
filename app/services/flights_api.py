from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
hotel_api_key = os.getenv("API_KEY_HOTELS")

def pegar_passagens():
    url = "https://serpapi.com/search?"

# Parâmetros da requisição teste
    params = {
    "engine": "google_flights",  
    "api_key": hotel_api_key
    }   

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 

        data = response.json()
        
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")

pegar_passagens() 