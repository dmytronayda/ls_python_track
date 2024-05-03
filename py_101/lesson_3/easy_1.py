# numbers = [1, 2, 3]
# numbers[3] = 5

# Q: Will the code below raise an error?
# A: Yes, it will raise an error, because we try to assign the value out of list `numbers` range.

# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False


# def get_last_char(str):
#     last_char = str[-1]
#     return last_char


# print(get_last_char(str1) == "!")  # True
# print(get_last_char(str2) == "!")  # False
famous_words = "seven years ago..."
# print("Four score and " + famous_words)


munsters_description = "The Munsters are creepy and spooky."
# => 'The munsters are creepy and spooky.'
# print(munsters_description.swapcase())


str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."


flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino", "Hoppy"])

# print(flintstones)


advice = "Few things in life are as important as house training your pet dinosaur."
# Expected return value:
# => 'Few things in life are as important as '
end_index = advice.find("house")
first_part = advice[0:end_index]
# print(first_part)

print(advice.replace("important", "urgent"))
