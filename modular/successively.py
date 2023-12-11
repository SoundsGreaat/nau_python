from core import worker, speed_test, base_currency, target_currency, dates


@speed_test
def successively_way(base_currency, target_currency, dates):
    print('Successively way:')
    for date in dates:
        worker(base_currency, target_currency, date)
    print()


if __name__ == "__main__":
    successively_way(base_currency, target_currency, dates)
