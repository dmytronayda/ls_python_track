# # # Will the following functions return the same results?


# # def first():
# #     return {
# #         "prop1": "hi there",
# #     }


# # def second():
# #     return
# #     {
# #         "prop1": "hi there",
# #     }


# # print(first())  # { "prop1": "hi there", }
# # print(second())  # value on line 12 is unreachable due to indentation issue, ruterns None


# dictionary = {"first": [1]}
# num_list = dictionary["first"]  # [1]
# num_list.append(2)  # [1, 2]

# print(num_list)  # [1, 2]
# print(dictionary)  # {"first": [1, 2]}


# def mess_with_vars(one, two, three):
#     one = two
#     two = three
#     three = one


# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")  # ["two"]
# print(f"two is: {two}")  # ["three"]
# print(f"three is: {three}")  # ["one"]


# def mess_with_vars(one, two, three):
#     one = ["two"]
#     two = ["three"]
#     three = ["one"]


# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")  # ["one"]
# print(f"two is: {two}")  # ["two"]
# print(f"three is: {three}")  # ["three"]


# def is_an_ip_number(str):
#     if str.isdigit():
#         number = int(str)
#         return 0 <= number <= 255
#     return False


# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     if len(dot_separated_words) != 4:
#         return False
#     for word in dot_separated_words:
#         if not is_an_ip_number(word):
#             return False
#     return True


# print(is_dot_separated_ip_address("124.10.55.20"))  # True
# print(is_dot_separated_ip_address("256.10.55.20"))  # False
# print(is_dot_separated_ip_address(input_string="256.10.55"))  # False
# print(is_dot_separated_ip_address(input_string="1000-55"))  # False

if False:
    greeting = "hello world"

print(greeting)  # NameError
