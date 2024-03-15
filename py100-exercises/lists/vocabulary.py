vocabulary = [
    ["happy", "cheerful", "merry", "glad"],
    ["tired", "sleepy", "fatigued", "drained"],
    ["excited", "eager", "enthused", "animated"],
]


def flatten(elements):
    result = []
    for row in elements:
        result += row
    return result


print(
    flatten(vocabulary)
)  # ['happy', 'cheerful', 'merry', 'glad', 'tired', 'sleepy', 'fatigued', 'drained', 'excited', 'eager', 'enthused', 'animated']
