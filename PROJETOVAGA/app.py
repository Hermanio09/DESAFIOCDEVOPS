import json
import time
import os
import requests
from datetime import datetime

# Função para pegar o clima atual da cidade
def pegar_clima(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br"
    response = requests.get(url)
    return response.json()

# Função para gerar o JSON com as informações do clima e salvar no caminho especificado
def gerar_json(caminho_arquivo, lat, lon, api_key):
    index = 0  # Contador para o ID do clima

    # Abre o arquivo JSON para escrita
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write("[")

    while True:
        clima = pegar_clima(lat, lon, api_key)

        index_data = {
            "index": {
                "_index": "clima_atual",
                "_id": index
            }
        }

        clima_info = {
            "@timestamp": datetime.now().isoformat(),
            "Data": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            "Clima": clima
        }

        # Adiciona o index_data e clima_info ao arquivo JSON
        with open(caminho_arquivo, "a", encoding="utf-8") as f:
            if index > 0:
                f.write(",\n")  # Adiciona uma quebra de linha antes de cada novo objeto JSON
            json.dump(index_data, f, ensure_ascii=False)
            f.write("\n")  # Adiciona uma quebra de linha entre index_data e clima_info
            json.dump(clima_info, f, ensure_ascii=False)

        print(f"Informação do clima adicionada ao arquivo '{caminho_arquivo}'")
        index += 1  # Incrementa o índice do clima
        time.sleep(60)  # Espera 1 minuto

if __name__ == "__main__":
    # Define o caminho do arquivo diretamente aqui
    caminho_arquivo = "logs/clima_atual.json"

    # Latitude e Longitude de Fortaleza, Ceará
    lat = -3.71722
    lon = -38.5433

    # Chave de API do OpenWeatherMap diretamente no código
    api_key = "24b7c1745c0606680c7aa976c759921e"

    gerar_json(caminho_arquivo, lat, lon, api_key)
