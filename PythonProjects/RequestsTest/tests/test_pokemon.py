import requests
import pytest  


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cae3a66810d54381094c497ffe593a58'
HEADER = {'Content-Type':'application/json', 'trainer_token' :TOKEN}



def test_trainers():    
    response = requests.get(url = f'{URL}/trainers')
    assert response. status_code == 200