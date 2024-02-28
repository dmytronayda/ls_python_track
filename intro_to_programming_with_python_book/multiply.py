num1 = float(input("Enter the first number: "));
num2 = float(input("Enter the second number: "));

def multiply(num1, num2):
    product = num1 * num2
    message = f"{num1} * {num2} = {product}"
    return message

print(multiply(num1, num2))