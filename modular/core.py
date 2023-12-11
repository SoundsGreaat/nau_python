import requests
from datetime import datetime


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


if __name__ == '__main__':
    base_currency = 'USD'
    target_currency = 'CZK'
    date = '12-10-2023'

    currency_rate = CurrencyRate(base_currency, target_currency, date)
    currency_rate.process_data()
    print(currency_rate)
