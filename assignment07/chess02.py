import time
import asyncio

my_compute_time = 0.1
opponent_compute_time = 0.5
opponents = 24
move_pairs = 30

async def game(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(my_compute_time)
        print(f"BOARD-{x+1} {i+1} Judit made a move.")
        await asyncio.sleep(opponent_compute_time)
        print(f"BOARD-{x+1} {i+1} Opponent made move.")
    duration = round(time.perf_counter() - board_start_time)
    print(f"BOARD-{x+1} - >>>>>>>>>>>>>>> Finished move in {duration} secs\n")
    return duration

async def main():
    task = [game(board) for board in range(opponents)]
    results = await asyncio.gather(*task)
    total_time = results
    print(f"Board exhibition finished in {total_time} secs.")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")
