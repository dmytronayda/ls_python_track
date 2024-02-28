ANNUAL_INTEREST_RATE = 0.05

def deposit_growth(cash, years):
    balance = 0 + cash
    for year in range(years):
        balance *= 1 + ANNUAL_INTEREST_RATE
    return f"""Your balance after {years} years of deposit
    with annual interest rate of {ANNUAL_INTEREST_RATE:.0%}
    will be ${round(balance, 2)}"""

print(deposit_growth(1000, 5))