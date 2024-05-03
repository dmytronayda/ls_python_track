# numbers = [1, 2, 3, 4]
# numbers.clear()

# print(numbers)


# print([1, 2, 3] + [4, 5])  # [1, 2, 3, 4, 5]

# str1 = "hello there"
# str2 = str1
# str2 = "goodbye!"
# print(str1)  # "hello there"


# my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
# my_list2 = my_list1.copy()
# my_list2[0]["first"] = 42
# print(my_list1)  # [{"first": 42}, {"second": "value2"}, 3, 4, 5]


def is_color_valid(color):
    return True if color == "blue" or color == "green" else False


print(is_color_valid("blue"))
