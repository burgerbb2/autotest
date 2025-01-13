import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '69e64c7e3dfc0f90cda0f0c68cd522c1'
TRAINER_ID = '12717'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }

body_pokemona = {
    'name': 'pokemons',
    'photo_id': 2
}

body_izmenit_name = {
    "pokemon_id": "191507",
    "name": "Изменилимяzz",
    "photo_id": 6
}

body_poimat = {
    "pokemon_id": "191507"
}

response_sozdat_pokemona = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemona)
print(response_sozdat_pokemona.text)

response_izmenit_pokemona = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_izmenit_name)
print(response_izmenit_pokemona.text)

response_poimat = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_poimat)
print(response_poimat.text)