destinations = [
    "Prague",
    "London",
    "Sydney",
    "Belfast",
    "Rome",
    "Aruba",
    "Paris",
    "Bora Bora",
    "Barcelona",
    "Rio de Janeiro",
    "Marrakesh",
    "New York City",
]


def contains(elem, elements):
    return True if elements.count(elem) else False


print(contains("Barcelona", destinations))  # True
print(contains("Nashville", destinations))  # False
print(contains("Lebedyn", destinations))  # False
print(contains("Lwiw", destinations))  # False
