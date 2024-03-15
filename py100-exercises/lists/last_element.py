def last(elements):
    if len(elements) > 0:
        last_index = len(elements) - 1
        return elements[last_index]
    return "Error: element not found."


print(last(["Earth", "Moon", "Mars"]))  # Mars
print(last(["Moon", "Earth"]))  # Earth
print(last([]))  #  Error: element not found.
