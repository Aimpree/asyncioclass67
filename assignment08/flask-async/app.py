from flask import Flask, render_template
import asyncio
import httpx
import time
import random
from pypokemon.pokemon import Pokemon

app = Flask(__name__)

async def get_pokemon(client, url):
    print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    pokemon = resp.json()

        
    return Pokemon(pokemon)

async def get_pokemons():
    async with httpx.AsyncClient() as client:
        tasks = []
        rand_list = []
        ab = []
        
        for i in range(1,151):
            rand_list.append(i)

        for number in rand_list:
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(get_pokemon(client, url))
            

        pokemons = await asyncio.gather(*tasks)
        Battle_ar_pokemons = [poke for poke in pokemons if poke.abilities["ability"]["name"] == "speed-boost" ] 
        print(ab.append(Battle_ar_pokemons))
        return Battle_ar_pokemons

@app.route('/')
def index():
    start_time = time.perf_counter()
    pokemons = asyncio.run(get_pokemons())
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")
    return render_template('index.html', pokemons=pokemons, end_time=end_time, start_time=start_time)

if __name__ == '__main__':
    app.run(debug=True, port=50001)
