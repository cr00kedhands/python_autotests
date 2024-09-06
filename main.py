import requests
import credentials

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = credentials.TOKEN
HEADERS = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
Body_create = {
    "name": "generate",
    "photo_id": -1
}

Create = requests.post(url= f'{URL}/pokemons', headers = HEADERS, json=Body_create)

Body_change = {
    "pokemon_id": Create.json()['id'],
    "name": "New Name",
    "photo_id": -1
}
Update = requests.put(url=f'{URL}/pokemons',headers=HEADERS, json = Body_change)

Pokemon_id = {'pokemon_id': Create.json()['id']}

AddPokebol = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADERS, json = Pokemon_id)
print(AddPokebol.text)