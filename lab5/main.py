import requests
from datetime import datetime, timedelta

items = []


class CurrencyRate:
    def __init__(self, base_currency, target_currency, start_date, end_date):
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.start_date = datetime.strptime(start_date, '%d-%m-%Y').date()
        self.end_date = datetime.strptime(end_date, '%d-%m-%Y').date()

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
        current_date = self.start_date
        while current_date <= self.end_date:
            exchange_rate = self.get_exchange_rate(current_date)

            item = {'date': current_date, 'exchange_rate': exchange_rate}
            items.append(item)

            current_date += timedelta(days=1)

    def __str__(self):
        value = ''
        for item in items:
            value += f'Date: {item["date"]}, Exchange Rate: {item["exchange_rate"]}\n'
        return value


base_currency = 'USD'
target_currency = 'CZK'
start_date = '01-01-2023'
end_date = '01-02-2023'

currency_rate = CurrencyRate(base_currency, target_currency, start_date, end_date)
currency_rate.process_data()
print(currency_rate)
