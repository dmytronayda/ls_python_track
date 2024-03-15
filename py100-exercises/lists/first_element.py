def first(elements):
    return elements[0] if len(elements) > 0 else "Error: element not found."


print(first(["Earth", "Moon", "Mars"]))  # Earth
print(first(["Moon", "Mars"]))  # Moon
print(first([]))  #  Error: element not found.
