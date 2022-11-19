import asyncio
import statistics
import timeit

from client import calculate_input
from generator import generate_data

time_taken = []
async def run_round(i, rounds):
    print(f"round {i} out of {rounds}")
    start = timeit.default_timer()
    data = generate_data()
    calculate_input(data)
    time_taken.append(timeit.default_timer() - start)


async def test_algo():
    rounds = 100
    background_tasks = set()
    for i in range(rounds):
        task = asyncio.create_task(run_round(i, rounds))
        background_tasks.add(task)
        task.add_done_callback(background_tasks.discard)
    await asyncio.gather(*background_tasks)
    print(f"ran {rounds} where the average time is {statistics.fmean(time_taken)}")


if __name__ == "__main__":
    asyncio.run(test_algo())
