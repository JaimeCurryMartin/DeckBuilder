import json
from collections import defaultdict

with open('/Users/administrador/Documents/DeckBuilder/clear_data/cartas_filtradas.json') as f:
    cards = json.load(f)

with open('/Users/administrador/Documents/DeckBuilder/buscar_patron/patrones_habilidad.json') as f:
    abilities_list = json.load(f)

with open('/Users/administrador/Documents/DeckBuilder/buscar_patron/patrones_type.json') as f:
    types_list = json.load(f)

types_count = defaultdict(int)
abilities_count = defaultdict(int)

for card in cards:
    card_types = card.get('type', '')
    for t in types_list:
        if t.lower() in card_types.lower():
            types_count[t] += 1
    
    card_text = card.get('text', '')
    for ability in abilities_list:
        if ability.lower() in card_text.lower():
            abilities_count[ability] += 1

sorted_types_count = dict(sorted(types_count.items(), key=lambda item: item[1], reverse=True))
sorted_abilities_count = dict(sorted(abilities_count.items(), key=lambda item: item[1], reverse=True))

result = {
    "types_count": sorted_types_count,
    "abilities_count": sorted_abilities_count
}

with open('/Users/administrador/Documents/DeckBuilder/buscar_patron/result.json', 'w') as f:
    json.dump(result, f, indent=4)

print(json.dumps(result, indent=4))
