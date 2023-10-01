def calculate_monthly_interest(principal_, annual_rate):
    monthly_rate = (annual_rate / 100) / 12
    return principal_ * monthly_rate


def calculate_total_amount(principal_, annual_rate, years_):
    total_amount_ = principal_
    for _ in range(years_ * 12):
        monthly_interest_ = calculate_monthly_interest(total_amount_, annual_rate)
        total_amount_ += monthly_interest_
    return total_amount_


while True:
    try:
        principal = float(input("Enter the deposit amount in UAH (at least 1000 UAH, in multiples of 1 UAH): "))
        if principal < 1000 or principal % 1 != 0:
            print("Deposit amount must be at least 1000 UAH and in multiples of 1 UAH.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    try:
        years = int(input("Enter the deposit term in years (3 to 5 years): "))
        if years < 3 or years > 5:
            print("Deposit term must be between 3 and 5 years.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

annual_interest_rate = 20

monthly_interest = calculate_monthly_interest(principal, annual_interest_rate)
total_amount = calculate_total_amount(principal, annual_interest_rate, years)

print("\nMonthly Interest Schedule:")
print(f"Initial Deposit: {principal} UAH")
print(f"Annual Interest Rate: {annual_interest_rate}%")
print(f"Deposit Term: {years} years\n")

for month in range(1, years * 12 + 1):
    print(f"Month {month}: {principal:.2f} UAH")
    principal += monthly_interest

print(f'\nTotal Amount After {years} years: {total_amount:.2f} UAH')
