import asyncio
from core import worker, speed_test, base_currency, target_currency, dates


async def process_date(base_currency, target_currency, date):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, worker, base_currency, target_currency, date)


@speed_test
async def async_way(base_currency, target_currency, dates):
    print('Async way:')

    tasks = [process_date(base_currency, target_currency, date) for date in dates]

    await asyncio.gather(*tasks)
    print()


if __name__ == "__main__":
    asyncio.run(async_way(base_currency, target_currency, dates))
