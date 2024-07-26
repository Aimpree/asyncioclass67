import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_dir = './assignment07/pokemon/pokemonapi'
pokemonmove_dir = './assignment07/pokemon/pokemonmove'

async def main():
    pathlist = Path(pokemonapi_dir).glob('*.json')

    # Iterate through all json files in the directory.
    for path in pathlist:
        async with aiofiles.open(f'{path}', mode='r') as f:
            content = await f.read()
            print(path)

        pokemon = json.loads(content)
        name = pokemon['name']
        moves = [move['move']['name'] for move in pokemon['moves']]

        async with aiofiles.open(f'{pokemonmove_dir}/{name}_moves.txt', mode='w') as f:
            await f.write('\n'.join(moves))

        
asyncio.run(main())
