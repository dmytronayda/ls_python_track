numbers = [3, 1, 5, 9, 2, 6, 4, 7]
plus_1_list = [element + 1
               for element in numbers
               if element < 5]

print(plus_1_list) # [4, 2, 3, 5]
