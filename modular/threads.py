import threading
from core import worker, speed_test, base_currency, target_currency, dates


@speed_test
def thread_way(base_currency, target_currency, dates):
    print('Thread way:')
    threads = []
    for date in dates:
        thread = threading.Thread(target=worker, args=(base_currency, target_currency, date))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print()


if __name__ == "__main__":
    thread_way(base_currency, target_currency, dates)
