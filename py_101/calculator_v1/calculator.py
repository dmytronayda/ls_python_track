import json

with open("calculator_messages.json", "r") as file:
    MESSAGES = json.load(file)

LANGUAGE = "de"


def prompt(message):
    print(f"=> {message}")


def messages(message, lang="en"):
    return MESSAGES[lang][message]


def invalid_number(num_str):
    try:
        int(num_str)
    except ValueError:
        return True

    return False


def calculate():
    prompt(messages("first_number", LANGUAGE))
    number1 = input()
    while invalid_number((number1)):
        prompt(messages("invalid_number_error", LANGUAGE))
        number1 = input()

    prompt(messages("second_number", LANGUAGE))
    number2 = input()
    while invalid_number((number2)):
        prompt(MESSAGES["invalid_number_error"])
        number2 = input()

    print(f"num 1 = {number1} and num2 = {number2}")

    prompt(messages("operations", LANGUAGE))
    operation = input()
    while operation not in ["1", "2", "3", "4"]:
        prompt(messages("invalid_operation_error", LANGUAGE))
        operation = input()

    match operation:
        case "1":
            result = int(number1) + int(number2)
        case "2":
            result = int(number1) - int(number2)
        case "3":
            result = int(number1) * int(number2)
        case "4":
            result = int(number1) / int(number2)

    prompt(messages("result", LANGUAGE) + str(result))


prompt(messages("welcome", LANGUAGE))
need_calculation = True

while need_calculation:
    calculate()
    prompt(messages("calculate_again", LANGUAGE))
    user_input = input().capitalize()
    while user_input not in messages("calculate_again_options", LANGUAGE):
        prompt(messages("invalid_option_error", LANGUAGE))
        user_input = input().capitalize()
    if user_input == "N":
        need_calculation = False
