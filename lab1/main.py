from datetime import date
from dateutil.relativedelta import relativedelta
from tabulate import tabulate


def calculate_deposit():
    while True:
        try:
            deposit_amount = int(input('Введіть суму вкладу: '))
            if deposit_amount < 1000:
                print('Мінімальна сума вкладу становить 1000 грн.')
            else:
                break
        except ValueError:
            print('Помилка, введіть число.')

    while True:
        try:
            deposit_term = int(input('Введіть строк вкладу (в роках): '))
            if deposit_term < 3 or deposit_term > 5:
                print('Строк вкладу повинен бути від 3 до 5 років.')
            else:
                break
        except ValueError:
            print('Помилка, введіть число.')

    annual_rate = 0.2
    monthly_rate = annual_rate / 12
    total_amount = deposit_amount
    current_date = date.today()
    tomorrows_date = current_date + relativedelta(days=1)
    month_counter = 1
    data = []

    print(f'\nДата оформлення: {current_date.strftime("%d/%m/%Y")}'
          f'\nДата початку дії договору: {tomorrows_date.strftime("%d/%m/%Y")}\n')
    print('Щомісячний графік нарахувань:')

    for year in range(deposit_term):
        monthly_interest = total_amount * monthly_rate
        total_amount_lock = total_amount
        for month in range(12):
            total_amount += monthly_interest
            if month_counter % 12 == 0:
                capitalization = f'+{total_amount - total_amount_lock:.2f} грн.'
            elif (month_counter - 1) % 12 == 0 and year != 0:
                capitalization = '<- капіталізація суми'
            else:
                capitalization = ''

            data.append([month_counter, tomorrows_date.strftime('%d/%m/%Y'), f'{total_amount:.2f} грн.',
                         f'+{monthly_interest:.2f} грн.', capitalization])
            month_counter += 1
            tomorrows_date += relativedelta(months=1)

    headers = ['Місяць', 'Дата', 'Загальна сума', 'Приріст', 'Капіталізація']
    print(tabulate(data, headers, tablefmt='pretty'))

    print(f'\nЗагальна сума: {total_amount:.2f} грн.')
    print(f'Дохід: {total_amount - deposit_amount:.2f} грн.')


if __name__ == '__main__':
    calculate_deposit()
