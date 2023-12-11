import asyncio
from core import base_currency, target_currency, dates
from successively import successively_way
from threads import thread_way
from async_ import async_way
import os

os.remove('results.txt') if os.path.exists('results.txt') else None

successively_way(base_currency, target_currency, dates)
thread_way(base_currency, target_currency, dates)
asyncio.run(async_way(base_currency, target_currency, dates))
