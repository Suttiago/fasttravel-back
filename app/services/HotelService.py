from dotenv import load_dotenv
import os
import requests
import json
from serpapi.google_search import GoogleSearch

load_dotenv()
hotel_api_key = os.getenv("API_KEY_HOTELS")

url = "https://serpapi.com/search"
params = {
        "engine": "google_hotels",
        "q": "teresopolis",
        "check_in_date": "25-09-06",
        "check_out_date": "25-09-07",
        "adults": 1,
        "currency": "BRL",
        "gl": "br",
        "hl": "pt-br",
        "api_key": os.getenv("HOTEL_API_KEY")
    }
search = GoogleSearch(params)
results = search.get_dict()
print(json.dumps(results, indent=2, ensure_ascii=False))  
