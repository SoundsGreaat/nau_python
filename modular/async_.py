import asyncio
from datetime import datetime
from core import worker

base_currency = 'USD'
target_currency = 'CZK'
dates = ['12-10-2023', '13-10-2023', '14-10-2023']


async def process_date(date):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, worker, base_currency, target_currency, date)


async def async_way():
    print('Async way:')

    tasks = [process_date(date) for date in dates]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = datetime.now()

    asyncio.run(async_way())

    end_time = datetime.now()
    duration = end_time - start_time
    print(f'Total time taken (async way): {duration}')
