from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time
import random

async def get_pokemon(client, url):
    #print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    pokemon = resp.json()

    return Pokemon(pokemon)

async def get_pokemons():
    async with httpx.AsyncClient() as client:
        tasks = []
        rand_list = range(1, 251)

        for number in rand_list:
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(get_pokemon(client, url))

        pokemons = await asyncio.gather(*tasks)
        
        
        battle_armor_pokemons = [
            poke.name for poke in pokemons 
            if any(ability.name == 'battle-armor' for ability in poke.abilities)
        ]
        speed_boost_pokemons = [
            poke.name for poke in pokemons 
            if any(ability.name == 'speed-boost' for ability in poke.abilities)
        ]
        
        print(f"Pokémon with 'battle-armor' ability: {battle_armor_pokemons}")
        print(f"Pokémon with 'speed-boost' ability: {speed_boost_pokemons}")
        return battle_armor_pokemons, speed_boost_pokemons
    

async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")

if __name__ == '__main__':
   asyncio.run(index())