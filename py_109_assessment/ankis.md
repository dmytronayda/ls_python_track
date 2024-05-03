Question: What naming convention is used for this variable name: `four_score_and_seven_years_ago`? What type of variables use this naming convention in Python?
Answer: This is a **snake_case** formatting, which is used for variable and function names. 
**snake_case** names begin with a lowercase letter. If name contains multiple words, they are separated with the underscore `_`.

---

Question: What naming convention is used for this variable name: `DomesticCat`? What type of variables use this naming convention in Python?
Answer: This is a **PascalCase** formatting, which is used for class names.

---

Question: What naming convention is used for this variable name: `INTEREST_RATE`? What type of variables use this naming convention in Python?
Answer: This is a **SCREAMING_SNAKE_CASE** formatting, which is used for constants.

---

Question: What characters are allowed in names for variables, constants, and functions in Python?
Answer: Alphabetic (a-z, A-Z without umlauts, accents, and so on) and numeric characters only. The first character must be alphabetic. Underscores are also allowed, subject to limitations.

---

Question: What is a type coercion?
Answer: Type coercion is the process of converting a value of one type to another.

---

Question: What is an explicit type coercion?
Answer: Explicit type coercion occurs when a programmer intentionally employs various built-in functions to convert a value of one type to another.

---

Question: What will this code return `int("42")`?
Answer: The int function converts the string to an integer `42`.

---

Question: What will this code return `int("abc")`?
Answer: Attempting to convert a non-numeric string to an integer using `int()` will raise a `ValueError`.

---

Question: What will this code return `int(['42'])`?
Answer: Passing any other data type but string, floating point number, or boolean, like a list in this example will result in a `TypeError`.

---

Question: What will this code return `float("42")`?
Answer: The int function converts the string to a float `42.0`.

---

Question: What will this code return `float({"age": "31"})`?
Answer: Passing any other data type but string, integer number, or boolean, like a dictionary in this example will result in a `TypeError`.

---

Question: What will this code return `float("abc")`?
Answer: Attempting to convert a non-numeric string to an integer using `float()` will raise a `ValueError`.

---

Question: What will this code return `float("NaN")`?
Answer: Outputs `nan`. Floats have a special "Not-a-Number" value `nan`. Not-a-Number is the way to represent the missing value in the data.

---

Question: What will this code return `bool({})`?
Answer: Outputs `False` as an empty dictionary evaluates to `False in a boolean context.

---

Question: What is an implicit type coercion?
Answer: Implicit type conversion, AKA automatic data type conversion, is when Python automatically transforms one data type into another without the programmer's direct instruction.

---

Question: What will this code output `print(5 + 5.10)`?
Answer: The `print` invocation outputs the value `10.10`. This code demonstrates Python's implicit type coercion rules, specifically how when you conduct a calculation involving both an integer and a float, the system will automatically adjust the integer to a float, ensuring the outcome is a float as well.

---

Question: What will this code output `print("Age:", 31)`?
Answer: The `print` invocation outputs the value "Age: 31". This code demonstrates Python's implicit type coercion rules, specifically how when using the `,` operator inside the `print()` function, Python will implicitly convert the non-string to a string.

---

Question: What will this code output `print(int("abc"))`?
Answer: The `print` invocation raises a `ValueError`, because attempting to convert a non-numeric string to an integer using `int()` function raises an Error.

---

Question: What will this code output `print(5 / 0)`?
Answer: The `print` invocation raises a `ZeroDivisionError`, because attempting to divide a number by zero.

---

Question: What will this code output `print(40 % 0)`?
Answer: The `print` invocation raises a `ZeroDivisionError`, because attempting to use `0` on the right side of the modulus operator.

---

Question: What is a string?
Answer: A string is a text sequence of Unicode characters in a specific sequence. Python uses strings to work with text data like names, messages and descriptions. You can write string literals with single, double or triple quotes.

---

Question: What is a literal?
Answer: A literal is any syntactic notation that lets you directly represent an object in source code.

---

Question: What will this code output `print('Dima'[0])`?
Answer: The `print` invocation outputs character `D`. You can access individual characters in a string with the `[]` indexing syntax.

---

Question: What will this code output `print(f'5 equals 5 is {5 == 5}.')`
Answer: The `print` invocation outputs the string `5 equals 5 is True`, because of string interpolation enabled by the use of an f-string. Specifically, Python replaces `{5 == 5}` substring with the value of the expression inside the braces.

---

Question: Write some code to print a string that contains the same value, but using all lowercase letters except for the first character, which should be capitalized.
```python
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
```
Answer: `print(munsters_description.capitalize())`

---

Question: Write some code to print a string with the case of all letters swapped:
```python
munsters_description = "the Munsters are CREEPY and Spooky."
# => "tHE mUNSTERS ARE CREEPY AND SPOOKY."
```
Answer: `print(munsters_description.swapcase())`

---

Question: Write some code to determine whether the name `Dino` appears in the strings below -- check each string separately:
```python
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Dino is a great guy who comes to CrossFit with his wife Nadine."
```
Answer: 
`print("Dino" in str1)  # False`
`print("Dino" in str2)  # True`

---

Question: Write some code to print a string "dima" with the case of all letters converted to uppercase.
Answer: `print("dima".upper()) # DIMA`

---

Question: Write some code to print a string "DIMA" with the case of all letters converted to lowercase.
Answer: `print("DIMA".lower()) # dima`

---

Question: Given the string "dima1", write some code to determine whether all characters in the string are alphabetic
Answer: `print("dima1".isalpha()) # False`

---

Question: Given the string "dima1", write some code to determine whether all characters in the string are digits
Answer: `print("dima1".isdigit()) # False`

---

Question: Given the string "dima1", write some code to determine whether all characters in the string are lower case
Answer: `print("dima1".islower()) # True`

---

Question: Given the string "DIMA1", write some code to determine whether all characters in the string are upper case
Answer: `print("DIMA1".isupper()) # True`

---

Question: Given the string "    " (4 whitespace chars), write some code to determine whether all characters in the string are whitespace characters
Answer: `print("    ".isspace()) # True`

---

Question: Given the string "    dima" (4 whitespace chars + "dima"), write some code to remove all whitespace characters and return string "dima"
Answer: `print("    dima".strip()) # "dima"`

---

Question: Given the string "    dima  " (4 whitespace chars + "dima" + 2 whitespace chars), write some code to remove whitespace characters before the substring "dima  "
Answer: `print("    dima  ".lstrip()) # "dima  "`

---

Question: Given the string "    dima  " (4 whitespace chars + "dima" + 2 whitespace chars), write some code to remove whitespace characters after the substring "    dima"
Answer: `print("    dima  ".rstrip()) # "    dima"`

---

Question: Given the string "dima Dima DIMA", write some code to replace all occurences of the substring "dima" replaced by "Olena"
Answer: `print("dima Dima dima".replace("dima", "Olena")) # "Olena Dima Olena"`

---

Question: Given the string "dima_Dima_DIMA", write some code to convert it to a list of names ['dima', '', 'Dima', 'DIMA']
Answer: `print("dima__Dima_DIMA".split("_")) # ['dima', '', 'Dima', 'DIMA']`

---

Question: Given the string "dima_dima_dima", write some code to define the first index position of the substring "dima"
Answer: `print("dima_dima_dima".find("dima"))  # 0`

---

Question: Given the string "dima_dima_dima", write some code to define the last index position of the substring "dima"
Answer: `print("dima_dima_dima".rfind("dima"))  # 10`

---

Question: Give 2 codes examples of short-circuiting behavior with logical operator `and`.
Answer: `and` short-circuits, stops evaluating when it encounters the first sub-expression from left-to-right that evaluates to `False`
```python
print(False and len(None))  # False
print([] and len(None))  # []
```

---

Question: Give 2 codes examples of short-circuiting behavior with logical operator `or`.
Answer: `or` short-circuits, stops evaluating when it encounters the first sub-expression from left-to-right that evaluates to `True`
```python
print(True and len(None))  # True
print("Dima" or len(None))  # Dima
```

---

Question: Give a code example that demonstrates a distinction between value's truthiness and its equality to `True`. 
Answer: 
```python
num = 5.0
if num:
    print(
        f"The value {num} is truthy. However, comparing {num} == True returns {num == True}"
    )
else:
    print(f"The value {num} is falsy.")
```

---

Question: What is `None`?
Answer: `None` is a data type in Python used to express the absense of a value. It can also indicate missing or unavailable data.

---

Question: What is a `range`? Give a code example that demonstrates a range of odd integers starting a 1 and ending with 9.
Answer: A range is a sequence of integers between two endpoints. Ranges are most commonly used to iterate over an increasing or decreasing range of integers.
```python
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
```

---

Question: Why does this code outputs `range(1, 10, 2)` and not a list of numbers `[1, 3, 5, 7, 9]`? Change the code to print the expected list of numbers.
```python
print(range(1, 10, 2))  # outputs "range(1, 10, 2)" not "[1, 3, 5, 7, 9]"
```
Answer: Python optimizes ranges to save memory. One way to get those numbers is to convert the range to a list or tuple. We can use the list and tuple functions to expand each range; either will suffice.
```python
odd_nums = list(range(1, 10, 2))
print(odd_nums)  # "[1, 3, 5, 7, 9]"
```

---

Question: Write two distinct ways of reversing the list without mutating the original list.
```python
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
```
Answer: 
```python
reversed_numbers_one = numbers[::-1]
reversed_numbers_two = list(reversed(numbers))
```

---

Question: Given a number and a list, determine whether the number is included in the list.
```python
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)
```
Answer: 
```python
number1 in numbers  # False
number2 in numbers  # True
```

---

Question: Given a list of numbers `[1, 2, 3, 4, 5]`, mutate the list by removing the number at index 2, so that the list becomes `[1, 2, 4, 5]`.
Answer: 
```python
numbers = [1, 2, 3, 4, 5]
del numbers[2]
print(numbers)  # [1, 2, 4, 5]
```

---

Question: How would you verify whether the data structures assigned to the variables numbers and table are of type list?
```python
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
```
Answer: 
```python
isinstance(numbers, list)  # True
isinstance(table, list)    # False
```

---

Question: Determine whether the following dictionary of people and their age contains an entry for 'Spot':
```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
```
Answer: 
```python
'Spot' in ages
```

---

Question: We have most of the Munster family in our ages dictionary:
```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
```
Add entries for Marilyn and Spot to the dictionary:
```python
additional_ages = {'Marilyn': 22, 'Spot': 237}
```
Answer: 
```python
ages.update(additional_ages)
```

---

Question: Write two different ways to remove all of the elements from the following list:
```python
numbers = [1, 2, 3, 4]
```
Answer: 
```python
numbers.clear() # Approach 1

while numbers:  # Approach 2
   numbers.pop()
```

---

Question: What will the following code output?
```python
print([1, 2, 3] + [4, 5])
```
Answer: In Python, you can use the `+` operator to concatenate two lists. This operation merges the second list into the first one, producing a new combined list.
```python
[1, 2, 3, 4, 5]
```