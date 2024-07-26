import aiofiles
import asyncio
import json

pokemonapi_dir = 'assignment07\pokemon\pokemonapi'
pokemonmove_dir = 'assignment07\pokemon\pokemonmove'

async def main():
    async with aiofiles.open(f'{pokemonapi_dir}/articuno.json', mode='r') as f:
        content = await f.read()

    pokemon = json.loads(content)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]
    
    async with aiofiles.open(f'{pokemonmove_dir}/{name}_moves.txt', mode='w') as f:
        await f.write('\n'.join(moves))




asyncio.run(main())