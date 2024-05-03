# # How to slice list elements and reverse them
# # list_name[start:stop:step]

# numbers = [1, 2, 3, 4, 5]
# reversed_nums = list(reversed(numbers))

# # print(reversed_nums)

# reversed_numbers = numbers[::-1]
# # print(reversed_numbers)

# # determine if element is in the list

# numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

# number1 = 8  # False
# number2 = 95  # True

# # print(number1 in numbers)  # using in keyword
# # print(number2 in numbers)

# print(31 in range(25, 67))  # True
# print(101 in range(100, 101))  # False, 101 is not included in range

# numbers = [1, 2, 3, 4, 5]
# # numbers.remove(3) removes by value
# numbers.pop(2)
# print(numbers)  # [1, 2, 4, 5]
# del numbers[2]
# print(numbers)  # [1, 2, 5]


# numbers = [1, 2, 3, 4]
# table = {"field1": 1, "field2": 2, "field3": 3, "field4": 4}

# print(type(numbers) is list)
# print(type(table) is list)

# table_len = 40
# title = "Flintstone Family Members"


# def get_padding(content_len, title):
#     title_len = len(title)
#     NUM_SIDES = 2
#     SPACE = " "

#     padding_len = (content_len - title_len) / NUM_SIDES - 1
#     padding_left = SPACE * int(padding_len)
#     return padding_left


# print(get_padding(table_len, title), title)
# print(title.center(40))


# statement1 = "The Flintstones Rock!"
# statement2 = "Easy come, easy go."

# print(statement1.count("t"))
# print(statement2.count("t"))


# ages = {"Herman": 32, "Lily": 30, "Grandpa": 402, "Eddie": 10}
# print("Spot" in ages)


ages = {"Herman": 32, "Lily": 30, "Grandpa": 5843, "Eddie": 10}
additional_ages = {"Marilyn": 22, "Spot": 237}

ages.update(additional_ages)
print(ages)
