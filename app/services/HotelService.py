from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
hotel_api_key = os.getenv("API_KEY_HOTELS")

def pegar_hoteis():
    url = "https://serpapi.com/search"

# Parâmetros da requisição teste
    params = {
    "engine": "google_hotels",  
    "q":"governador valadares",
    "check_in_date": "2025-08-29",
    "check_out_date": "2025-10-02",
    "api_key": hotel_api_key
    }   

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 

        data = response.json()
        
        
        #array que vai listar os hoteis

        hotels = data.get("properties",[])
        hotel_list = []
        for hotel in hotels:
            hotel_info ={
            "name": hotel.get("name"),
            "description":hotel.get("description"),
            "link":hotel.get("link")}
            
            hotel_list.append(hotel_info)
            
        return hotel_list
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}") 


hoteis = pegar_hoteis()
for hotel in hoteis:
    print(json.dumps(hotel, indent=4, ensure_ascii=False))
