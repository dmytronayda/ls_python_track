def prompt(message):
    print(f"=> {message}")


def invalid_number(num_str):
    try:
        int(num_str)
    except ValueError:
        return True

    return False


prompt("Welcome to Calculator!")

prompt("What's the first number?")
number1 = input()
while invalid_number((number1)):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()
while invalid_number((number2)):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

print(f"num 1 = {number1} and num2 = {number2}")

prompt(
    "What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide"
)
operation = input()
while operation not in ["1", "2", "3", "4"]:
    prompt("You must choose 1, 2, 3, or 4")
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

prompt(f"The result is {result}")
