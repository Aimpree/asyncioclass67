import asyncio
from time import sleep, time
from random import random

async def fry_rice():
    timer = 1 + random()
    print(f'cooking Fry rice in {timer} sec')
    await asyncio.sleep(timer)
    return f'Fry rice done in {timer} sec'

async def make_noodle():
    timer = 1 + random()
    print(f'cooking Fry noodle in {timer} sec')
    await asyncio.sleep(timer)
    return f'noodle done in {timer} sec'

async def make_curry():
    timer = 1 + random()
    print(f'cooking Curry in {timer} sec')
    await asyncio.sleep(timer)
    return f'Curry done in {timer} sec'

async def main():
    tasks = [asyncio.create_task(fry_rice()),
             asyncio.create_task(make_noodle()),
             asyncio.create_task(make_curry())]
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # print("real out put:")
    # for task in tasks:
    #     result_output = await task 
    #     print(f'Task result: {result_output}')
    
    print("Done:")
    for task in done:
        print(f'Task result: {task.result()}')
    
    print("\nPending:")
    for task in pending:
        result = await task
        print(f'Pending task result: {result}')

asyncio.run(main())
