SPACE = " "


def capitalize_words(string):
    words = string.split(" ")
    result = []
    for word in words:
        result.append(word.capitalize())
    return SPACE.join(result)


print(capitalize_words("launch school tech & talk."))  # 'Launch School Tech & Talk '
print(capitalize_words("Dima learns python now."))  # 'Dima Learns Python Now '
