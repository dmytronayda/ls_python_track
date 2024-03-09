# my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

# while index < len(my_list):
#     elem = my_list[index]
#     if is_odd(elem):
#         print(elem)
#     index += 1

# for elem in my_list:
#     if is_odd(elem):
#         print(elem)

# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# for line in my_list:
#     for elem in line:
#         if (is_even(elem)):
#             print(elem)

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

def print_odd_even(iterable):
    for elem in iterable:
        print("odd" if is_odd(elem) else "even")

# print_odd_even(my_list)

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def isInt(elem):
    return type(elem) is int

def find_integers(tuple_element):
    return [element
            for element in tuple_element
            if isInt(element)]

integers = find_integers(my_tuple)
# print(integers)                    # [1, 3, -4]

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result = {elem : len(elem)
       for elem in my_set
       if is_odd(len(elem))}

print(result)