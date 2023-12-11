import asyncio
from successively import successively_way
from threads import thread_way
from async_ import async_way
from datetime import datetime

start_time_successively = datetime.now()
successively_way()
end_time_successively = datetime.now()
print()

start_time_thread = datetime.now()
thread_way()
end_time_thread = datetime.now()
print()

start_time_async = datetime.now()
asyncio.run(async_way())
end_time_async = datetime.now()

with open('results.txt', 'w+') as file:
    file.write(f'Successively way: {end_time_successively - start_time_successively}\n')
    file.write(f'Thread way: {end_time_thread - start_time_thread}\n')
    file.write(f'Async way: {end_time_async - start_time_async}\n')
