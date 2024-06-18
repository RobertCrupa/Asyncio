from __future__ import annotations

import asyncio

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
async def main():

    await concurrent_routines_2_10()

asyncio.run(main())
