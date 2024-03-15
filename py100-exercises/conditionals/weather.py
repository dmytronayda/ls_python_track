weather = 'sunny'

decisions = [
    "It's a beautiful day!",
    "Grab your umbrella.",
    "Let's stay inside."
]

# if weather == "sunny":
#     print(decisions[0])
# elif weather == "rainy":
#     print(decisions[1])
# else:
#     print(decisions[2])

match weather:
    case 'sunny':
        print(decisions[0])
    case 'rainy':
        print(decisions[1])
    case _:
        print(decisions[2])
