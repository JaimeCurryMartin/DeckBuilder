import json

def filtrar_campos_carta(carta):
    return {
        "name": carta.get("name", ""),
        "manaCost": carta.get("manaCost", ""),
        "colors": carta.get("colors", []),
        "type": carta.get("type", ""),
        "text": carta.get("text", "")
    }

def procesar_cartas(json_cartas):
    cartas_filtradas = [filtrar_campos_carta(carta) for carta in json_cartas]
    return cartas_filtradas


if __name__ == "__main__":
    with open('/Users/administrador/Documents/DeckBuilder/find_cards/info_cartas.json', 'r', encoding='utf-8') as file:
        cartas_json = json.load(file)

    cartas_filtradas = procesar_cartas(cartas_json)

    with open('/Users/administrador/Documents/DeckBuilder/clear_data/cartas_filtradas.json', 'w', encoding='utf-8') as file:
        json.dump(cartas_filtradas, file, indent=4, ensure_ascii=False)

    print("Nuevo JSON con campos filtrados generado.")