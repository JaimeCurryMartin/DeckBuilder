import requests
import re
import json

# Función para cargar y procesar el archivo de texto
def cargar_cartas_txt(file_path):
    cartas = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for linea in file:
            # Usar regex para extraer solo el nombre de la carta, ignorando lo que está antes y entre paréntesis y después
            match = re.match(r'\d+\s+([A-Za-z,\-\s\']+)', linea)
            if match:
                nombre_carta = match.group(1).strip()  # Obtener el nombre y eliminar espacios extra
                cartas.append(nombre_carta)
    return cartas

# Realizar la solicitud GET a la API de MTG y obtener solo la versión más reciente
def obtener_version_mas_nueva(nombre_carta):
    url = f"https://api.magicthegathering.io/v1/cards?name={nombre_carta}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        cartas = data.get("cards", [])
        
        if cartas:
            # Ordenar las cartas por fecha de lanzamiento ('releaseDate') y obtener la más reciente
            cartas_ordenadas = sorted(cartas, key=lambda x: x.get('releaseDate', '0000-00-00'), reverse=True)
            return cartas_ordenadas[0]  # Devolver la carta más reciente
        else:
            print(f"No se encontró ninguna carta con el nombre {nombre_carta}")
            return None
    else:
        print(f"Error al obtener la carta {nombre_carta}: {response.status_code}")
        return None

# Procesar la lista de cartas y obtener la información de la versión más reciente de cada una
def obtener_info_cartas(cartas):
    info_cartas = []
    for carta in cartas:
        info = obtener_version_mas_nueva(carta)
        if info:
            info_cartas.append(info)
    return info_cartas

# Guardar la información de las cartas en un archivo JSON con codificación UTF-8
def guardar_info_cartas(file_path, info_cartas):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(info_cartas, file, indent=4, ensure_ascii=False)

# Main
if __name__ == "__main__":
    # Path del archivo txt con los nombres de las cartas
    file_path = '/Users/administrador/Documents/DeckBuilder/load_cards/cardsList.txt'
    
    # Cargar los nombres de las cartas desde el archivo txt
    nombres_cartas = cargar_cartas_txt(file_path)

    # Obtener la información de la versión más reciente de cada carta
    info_cartas = obtener_info_cartas(nombres_cartas)

    # Guardar la información de las cartas en un archivo JSON
    guardar_info_cartas('info_cartas.json', info_cartas)
    print("Información de las cartas guardada en info_cartas.json")
