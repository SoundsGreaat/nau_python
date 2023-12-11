from datetime import datetime
from core import worker

base_currency = 'USD'
target_currency = 'CZK'
dates = ['12-10-2023', '13-10-2023', '14-10-2023']


def successively_way():
    print('Successively way:')
    for date in dates:
        worker(base_currency, target_currency, date)


if __name__ == "__main__":
    start_time = datetime.now()

    successively_way()

    end_time = datetime.now()
    duration = end_time - start_time
    print(f'Total time taken (successively way): {duration}')
