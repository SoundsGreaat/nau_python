import threading
from datetime import datetime
from core import worker

base_currency = 'USD'
target_currency = 'CZK'
dates = ['12-10-2023', '13-10-2023', '14-10-2023']


def thread_way():
    print('Thread way:')
    threads = []
    for date in dates:
        thread = threading.Thread(target=worker, args=(base_currency, target_currency, date))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = datetime.now()

    thread_way()

    end_time = datetime.now()
    duration = end_time - start_time
    print(f'Total time taken (thread way): {duration}')
