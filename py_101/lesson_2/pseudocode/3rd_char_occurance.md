GET char = input char from the user
GET string = input string from the user
SET occurance = 0
SET index = 0

WHILE index < len(string)
    SET char_at_idx = string[index]
    IF occurance == 3
        RETURN index
    IF char_at_idx == char
        occurance += 1
    index += 1


