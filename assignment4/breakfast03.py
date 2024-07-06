# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee():
    print("coffee: prepare ingridients")
    await asyncio.sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5)
    print("coffee: ready")

async def fry_eggs():
    print("eggs: prepare ingridients")
    await asyncio.sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3)
    print("eggs: ready")

async def main():
    start = time()

    task1 = asyncio.create_task(make_coffee())
    task2 = asyncio.create_task(fry_eggs())

    result1 = await task1
    result2 = await task2
    print(result1,result2)
    print(f"breakfast is ready in {time()-start} min")


asyncio.run(main())