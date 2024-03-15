from locale2 import extract_region


def local_greet(locale):
    region = extract_region(locale)
    match region:
        case "US":
            return "Hey!"
        case "GB":
            return "Hello!"
        case "AU":
            return "Howdy!"
        case _:
            return "Error: unknown region code."


print(local_greet("en_US.UTF-8"))  # Hey!
print(local_greet("en_GB.UTF-8"))  # Hello!
print(local_greet("en_AU.UTF-8"))  # Howdy!
