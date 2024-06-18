from __future__ import annotations

import asyncio
from asyncio import CancelledError

from utils import async_timed
from utils import delay


@async_timed()
async def concurrent_routines_2_10() -> None:

    @async_timed()
    async def hello_every_second() -> None:
        for second in range(2):
            await asyncio.sleep(1)
            print(f'Hello from second {second}')

    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))

    await hello_every_second()
    await first_delay
    await second_delay


@async_timed()
async def cancell_routine_2_11() -> None:
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():
        print(f'Task not finished after {seconds_elapsed} seconds')

        await asyncio.sleep(1)

        seconds_elapsed += 1

        if seconds_elapsed == 4:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print(f'Task was cancelled after {seconds_elapsed} seconds')


@async_timed()
async def main():

    await cancell_routine_2_11()

asyncio.run(main())
