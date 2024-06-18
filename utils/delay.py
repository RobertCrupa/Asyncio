from __future__ import annotations

import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'sleeping for {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'Finished sleeping for {delay_seconds} seconds')
    return delay_seconds
