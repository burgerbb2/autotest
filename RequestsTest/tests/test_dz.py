import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '69e64c7e3dfc0f90cda0f0c68cd522c1'
TRAINER_ID = '12717'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }

def test_status_code():
    response_polushit = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_polushit.status_code == 200

def test_part_of_response():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.json()["data"][0]['name'] == 'Изменилимяzz'