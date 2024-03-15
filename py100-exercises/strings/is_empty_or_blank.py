def is_empty(str):
    return len(str) == 0


def is_blank(str):
    return str.isspace()


def is_empty_or_blank(str):
    return is_empty(str) or is_blank(str)


print(is_empty_or_blank("mars"))  # False
print(is_empty_or_blank("  "))  # True
print(is_empty_or_blank(""))  # True
