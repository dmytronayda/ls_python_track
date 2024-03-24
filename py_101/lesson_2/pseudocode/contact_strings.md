GET strings = list of strings
SET result = "" empty string
SET index = 0
WHILE index < len(strings)
    SET current_elem = strings[index]
    result += current_elem
RETURN result