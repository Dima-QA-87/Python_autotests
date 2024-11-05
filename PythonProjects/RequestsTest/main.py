import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cae3a66810d54381094c497ffe593a58'
HEADER = {'Content-Type':'application/json', 'trainer_token' :TOKEN}




body_create = {
    "name": "Pikachu",
    "photo_id": 22
}

payload = {
    "pokemon_id": "123413",
    "name": "Пикачу",
    "photo_id": 16
}

body_pokeball = {
    "pokemon_id": "123413"
}



'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(respons_create)'''

'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = payload)
print(payload)'''

'''response_create = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_create)'''
