import requests
import inspect
from datetime import datetime

base_currency = 'USD'
target_currency = 'CZK'
dates = ['12-10-2023', '13-10-2023', '14-10-2023']


class CurrencyRate:
    def __init__(self, base_currency, target_currency, date):
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.date = datetime.strptime(date, '%d-%m-%Y').date()
        self.items = []

    def get_exchange_rate(self, date):
        url = f'https://api.frankfurter.app/{date}?from={self.base_currency}'

        response = requests.get(url)

        if not response.ok:
            print(f'Error {response.status_code}: {response.text}')
            exit()

        data = response.json()
        exchange_rate = data['rates'][self.target_currency]

        return exchange_rate

    def process_data(self):
        exchange_rate = self.get_exchange_rate(self.date.strftime('%Y-%m-%d'))

        item = {'date': self.date, 'exchange_rate': exchange_rate}
        self.items.append(item)

    def __str__(self):
        value = ''
        for item in self.items:
            value += f'Date: {item["date"]}, Exchange Rate: {item["exchange_rate"]}'
        return value


def worker(base_currency, target_currency, date):
    currency_rate = CurrencyRate(base_currency, target_currency, date)
    currency_rate.process_data()

    print(currency_rate)


def speed_test(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()

        func(*args, **kwargs)

        end_time = datetime.now()
        duration = end_time - start_time
        print(f'Total time taken ({func.__name__}): {duration}\n')
        with open('results.txt', 'a+') as file:
            file.write(f'{func.__name__}: {duration}\n')

    async def async_wrapper(*args, **kwargs):
        start_time = datetime.now()

        await func(*args, **kwargs)

        end_time = datetime.now()
        duration = end_time - start_time
        print(f'Total time taken ({func.__name__}): {duration}\n')
        with open('results.txt', 'a+') as file:
            file.write(f'{func.__name__}: {duration}\n')

    if inspect.iscoroutinefunction(func):
        return async_wrapper
    return wrapper


if __name__ == '__main__':
    base_currency = 'USD'
    target_currency = 'CZK'
    date = '12-10-2023'

    currency_rate = CurrencyRate(base_currency, target_currency, date)
    currency_rate.process_data()
    print(currency_rate)
