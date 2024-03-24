GET elements = list of integers
SET every_other_elem = empty list
SET index = 0

WHILE index < len(elements)
    IF index is even number, like 0, 2, 4 ...
        SET element = elements[index]
        add element to every_other_elem

RETURN every_other_elem
