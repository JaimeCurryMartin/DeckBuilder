import requests
import re
import json

def cargar_cartas_txt(file_path):
    cartas = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for linea in file:
            match = re.match(r'\d+\s+([A-Za-z,\-\s\']+)', linea)
            if match:
                nombre_carta = match.group(1).strip() 
                cartas.append(nombre_carta)
    return cartas

def obtener_version_mas_nueva(nombre_carta):
    url = f"https://api.magicthegathering.io/v1/cards?name={nombre_carta}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        cartas = data.get("cards", [])
        
        if cartas:
            cartas_ordenadas = sorted(cartas, key=lambda x: x.get('releaseDate', '0000-00-00'), reverse=True)
            return cartas_ordenadas[0]  
        else:
            print(f"No se encontró ninguna carta con el nombre {nombre_carta}")
            return None
    else:
        print(f"Error al obtener la carta {nombre_carta}: {response.status_code}")
        return None

def obtener_info_cartas(cartas):
    info_cartas = []
    for carta in cartas:
        info = obtener_version_mas_nueva(carta)
        if info:
            info_cartas.append(info)
    return info_cartas

def guardar_info_cartas(file_path, info_cartas):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(info_cartas, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    file_path = '/Users/administrador/Documents/DeckBuilder/find_cards/cardsList.txt'
    
    nombres_cartas = cargar_cartas_txt(file_path)

    info_cartas = obtener_info_cartas(nombres_cartas)

    guardar_info_cartas('/Users/administrador/Documents/DeckBuilder/find_cards/info_cartas.json', info_cartas)
    print("Información de las cartas guardada en info_cartas.json")
