import json

with open("mortgage_calculator_messages.json", "r") as file:
    MESSAGES = json.load(file)

MONTHS_IN_YR = 12
LANGUAGE = "en"


def to_monthly_interest_rate(annual_interest):
    return (int(annual_interest) / MONTHS_IN_YR) / 100


def to_months(yrs):
    return int(yrs) * MONTHS_IN_YR


def monthly_payment(loan_amount, annual_interest, loan_duration_yrs):
    monthly_interest = to_monthly_interest_rate(annual_interest)
    duration_months = to_months(loan_duration_yrs)
    to_pay_monthly = int(loan_amount) * (
        monthly_interest / (1 - (1 + monthly_interest) ** (-duration_months))
    )
    return to_pay_monthly


def prompt(message_key, lang="en"):
    print(f"=> {MESSAGES[lang][message_key]}")


def invalid_number(num_str):
    try:
        int(num_str)
    except ValueError:
        return True

    return False


prompt("welcome", LANGUAGE)


prompt("loan_amount", LANGUAGE)

total_loan_amount = input()
while invalid_number((total_loan_amount)):
    prompt("invalid_loan_amount", LANGUAGE)
    total_loan_amount = input()

prompt("annual_interest", LANGUAGE)
annual_interest_rate = input()
while invalid_number((total_loan_amount)):
    prompt("invalid_loan_amount", LANGUAGE)
    annual_interest_rate = input()

prompt("loan_duration_yrs", LANGUAGE)
loan_duration = input()
while invalid_number((loan_duration)):
    prompt("invalid_loan_duration_yrs", LANGUAGE)
    loan_duration = input()


monthly_rate = monthly_payment(total_loan_amount, annual_interest_rate, loan_duration)
formated_monthly_rate = "{:.2f}".format(monthly_rate)

print(f"Your monthly payment will be: ${formated_monthly_rate}")
