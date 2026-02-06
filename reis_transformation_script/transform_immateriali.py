import json
import os
import uuid
import requests
from pydbpedia import PyDBpedia
from SPARQLWrapper import SPARQLWrapper, JSON

# === Configurazione ===
DBPEDIA_ENDPOINT = "http://dbpedia.org/sparql"
API_KEY = "YOUR_API_KEY_HERE"
INPUT_FILE = "data/immateriali_input.json"
OUTPUT_FILE = "output/ngsi_ld_immateriali_rivisto.jsonld"
CONTEXT_URL = "https://raw.githubusercontent.com/user/repo/main/context.jsonld"
LOCAL_CONTEXT_FILE = "context_local.jsonld"

# === Inizializza DBpedia ===
dbpedia = PyDBpedia(endpoint=DBPEDIA_ENDPOINT)

# === Mappatura categoria → URI DBpedia ===
category_mapping = {
    "Rappresentazione/Spettacolo": "http://dbpedia.org/resource/Performance",
    "Festa/Cerimonia": "http://dbpedia.org/resource/Festival",
    "Tecnica artigiana": "http://dbpedia.org/resource/Craft",
    "Tesoro umano vivente": "http://dbpedia.org/resource/Living_national_treasure",
    # ... (restante mappatura invariata)
}

# === Carica contesto ===
try:
    context = requests.get(CONTEXT_URL).json()
except:
    print("Avviso: Impossibile caricare il contesto remoto, procedo con configurazione locale.")

# === Carica entità City e Province (per geolocalizzazione) ===
headers = {
    "x-api-key": API_KEY,
    "Link": f'<{CONTEXT_URL}>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
    "Accept": "application/json"
}

print("Caricamento dati geografici...")
city_response = requests.get("https://your-api-endpoint.com/v1/entities?type=City", headers=headers)
province_response = requests.get("https://your-api-endpoint.com/v1/entities?type=Province", headers=headers)

cities = city_response.json() if city_response.status_code == 200 else []
provinces = province_response.json() if province_response.status_code == 200 else []

# === Mappe di lookup ===
province_locations = {}
province_names = {}
for province in provinces:
    p_id = province['id']
    province_names[p_id] = province.get('name', {}).get('value', '')
    location = province.get('location', {}).get('value', {})
    if location.get("type") == "Point":
        province_locations[p_id] = location.get("coordinates", [])

city_map = {}
for city in cities:
    name = city['name']['value'].lower()
    city_id = city['id']
    p_id = city.get('hasProvince', {}).get('object', '')
    location = city.get('location', {}).get('value', {})
    if location.get("type") == "Point":
        coords = location.get("coordinates", [])
        city_map[name] = {
            "id": city_id,
            "lon": coords[0],
            "lat": coords[1],
            "province_id": p_id,
            "province_name": province_names.get(p_id, "")
        }

# === Carica dati originali ===
print("Caricamento dati immateriali...")
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

# === Funzioni di Trasformazione ===
def parse_categories(raw):
    if not raw: return []
    return [x.strip().lower() for x in raw.replace(";", ",").split(",")]

def get_entity_type(categories):
    lowercase_mapping = {k.lower(): v for k, v in category_mapping.items()}
    for cat in categories:
        if cat in lowercase_mapping:
            return lowercase_mapping[cat]
    return "http://dbpedia.org/resource/Event"

def create_ngsi_ld_entry(item):
    # Logica di mapping (come nel tuo script originale)
    # ...
    return entity # (omesso per brevità, mantiene la tua logica)

# === Esecuzione ===
print("Creazione entità NGSI-LD...")
ngsi_ld_events = [create_ngsi_ld_entry(item) for item in data]

# Funzione update_context_file() e save_ngsi_ld_to_file() chiamate con i nuovi path costanti
