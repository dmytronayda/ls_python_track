scores = [96, 47, 113, 89, 100, 102]


def is_equal_or_more(minimum, elements):
    result = []
    for elem in elements:
        if elem >= minimum:
            result.append(elem)
    return len(result)


print(is_equal_or_more(100, scores))  # 3
