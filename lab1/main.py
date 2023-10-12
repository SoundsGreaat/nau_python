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

    print('Щомісячний графік нарахувань:')
    for i in range(deposit_term):
        print(f'\nРік {i + 1}:')
        monthly_interest = total_amount * monthly_rate
        for month in range(12):
            total_amount += monthly_interest
            print(f'Місяць {month + 1}: {total_amount:.2f} грн. | +{monthly_interest:.2f} грн.')

    print(f'Загальна сума: {total_amount:.2f} грн.')
    return


if __name__ == '__main__':
    calculate_deposit()
