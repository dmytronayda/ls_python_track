# Launch School PY109 Written Assessment Prep

Launch School Study guide: https://launchschool.com/lessons/1318de4f/assignments/ff1c7aa8 
PY101: https://launchschool.com/courses/c004809e/home 
Intro to Programming with Python: https://launchschool.com/books/python 
MD preview in VS Code: `SHIFT + CMD + V`


# naming conventions: legal vs. idiomatic, illegal vs. non-idiomatic
Style Guide: https://launchschool.com/lessons/a29e9831/assignments/fdec0cd9 

Question: What naming convention is used for this variable name: `four_score_and_seven_years_ago`? What type of variables use this naming convention in Python?
Answer: This is a **snake_case** formatting, which is used for variable and function names. **snake_case** names begin with a lowercase letter. If name contains multiple words, they are separated with the underscore `_`.

Question: What naming convention is used for this variable name: `DomesticCat`? What type of variables use this naming convention in Python?
Answer: This is a **PascalCase** formatting, which is used for class names. 

Question: What naming convention is used for this variable name: `INTEREST_RATE`? What type of variables use this naming convention in Python?
Answer: This is a **SCREAMING_SNAKE_CASE** formatting, which is used for constants. 

Qeustion: What characters are allowed in names for variables, constants, and functions in Python?
Aanswer: Alphabetic (a-z, A-Z without umlauts, accents, and so on) and numeric characters only. The first character must be alphabetic. Underscores are also allowed, subject to limitations.


# type coercions: explicit (e.g., using int(), str()) and implicit
Question: What is a type coercion?
Answer: Type coercion is the process of converting a value of one type to another.

Question: What is an explicit type coercion?
Answer: Explicit type coercion occurs when a programmer intentionally employs various built-in functions to convert a value of one type to another.

Question: What will this code return `int("42")`?
Answer: The int function converts the string to an integer `42`.

Question: What will this code return `int("abc")`?
Answer: Attempting to convert a non-numeric string to an integer using `int()` will raise a `ValueError`.

Question: What will this code return `int(['42'])`?
Answer: Passing any other data type but string, floating point number, or boolean, like a list in this example will result in a `TypeError`.

Question: What will this code return `float("42")`?
Answer: The int function converts the string to a float `42.0`.

Question: What will this code return `float({"age": "31"})`?
Answer: Passing any other data type but string, integer number, or boolean, like a dictionary in this example will result in a `TypeError`.

Question: What will this code return `float("abc")`?
Answer: Attempting to convert a non-numeric string to an integer using `float()` will raise a `ValueError`.

Question: What will this code return `float("NaN")`?
Answer: Outputs `nan`. Floats have a special "Not-a-Number" value `nan`. Not-a-Number is the way to represent the missing value in the data. 

Question: What will this code return `bool({})`?
Answer: Outputs `False` as an empty dictionary evaluates to `False in a boolean context. 

Question: What is an implicit type coercion?
Answer: Implicit type conversion, AKA automatic data type conversion, is when Python automatically transforms one data type into another without the programmer's direct instruction. 

Question: What will this code output `print(5 + 5.10)`?
Answer: The `print` invocation outputs the value `10.10`. This code demonstrates Python's implicit type coercion rules, specifically how when you conduct a calculation involving both an integer and a float, the system will automatically adjust the integer to a float, ensuring the outcome is a float as well.

Question: What will this code output `print("Age:", 31)`?
Answer: The `print` invocation outputs the value "Age: 31". This code demonstrates Python's implicit type coercion rules, specifically how when using the `,` operator inside the `print()` function, Python will implicitly convert the non-string to a string.


# numbers, including handling exceptions (ValueError, ZeroDivisionError)
Error types / Error handling: https://launchschool.com/lessons/a29e9831/assignments/378f8121 

Question: What will this code output `print(int("abc"))`?
Answer: The `print` invocation raises a `ValueError`, because attempting to convert a non-numeric string to an integer using `int()` function raises an Error.

Question: What will this code output `print(5 / 0)`?
Answer: The `print` invocation raises a `ZeroDivisionError`, because attempting to divide a number by zero.

Question: What will this code output `print(40 % 0)`?
Answer: The `print` invocation raises a `ZeroDivisionError`, because attempting to use `0` on the right side of the modulus operator.

# strings
https://launchschool.com/books/python/read/data_types#textsequences 

Question: What is a string?
Answer: A string is a text sequence of Unicode characters in a specific sequence. Python uses strings to work with text data like names, messages and descriptions. You can write string literals with single, double or triple quotes. 

Question: What is a literal?
Answer: A literal is any syntactic notation that lets you directly represent an object in source code. For instance, all of the following are literals in Python:
```python
'Hello, world!'   # str literal
3.141592          # float literal
True              # bool literal
{'a': 1, 'b': 2}  # dict literal
[1, 2, 3]         # list literal
(4, 5, 6)         # tuple literal
{7, 8, 9}         # set literal
```

Question: What will this code output `print('Dima'[0])`?
Answer: The `print` invocation outputs character `D`. You can access individual characters in a string with the `[]` indexing syntax.

# f-strings
Question: What will this code output `print(f'5 equals 5 is {5 == 5}.')`
Answer: The `print` invocation outputs the string `5 equals 5 is True`, because of string interpolation enabled by the use of an f-string. Specifically, Python replaces `{5 == 5}` substring with the value of the expression inside the braces.

# string methods
## capitalize, swapcase, upper, lower
Question: Write some code to print a string that contains the same value, but using all lowercase letters except for the first character, which should be capitalized.
```python
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
```

Answer: `print(munsters_description.capitalize())`


Question: Write some code to print a string with the case of all letters swapped:
```python
munsters_description = "the Munsters are CREEPY and Spooky."
# => "tHE mUNSTERS ARE CREEPY AND SPOOKY."
```
Answer: `print(munsters_description.swapcase())`

Question: Write some code to determine whether the name `Dino` appears in the strings below -- check each string separately:
```python
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Dino is a great guy who comes to CrossFit with his wife Nadine."
```
Answer: 
`print("Dino" in str1)  # False`
`print("Dino" in str2)  # True`

Question: Write some code to print a string "dima" with the case of all letters converted to uppercase.
Answer: `print("dima".upper()) # DIMA`

Question: Write some code to print a string "DIMA" with the case of all letters converted to lowercase.
Answer: `print("DIMA".lower()) # dima`

## isalpha, isdigit, isalnum, islower, isupper, isspace
Question: Given the string "dima1", write some code to determine whether all characters in the string are alphabetic
Answer: `print("dima1".isalpha()) # False`

Question: Given the string "dima1", write some code to determine whether all characters in the string are digits
Answer: `print("dima1".isdigit()) # False`

Question: Given the string "dima1", write some code to determine whether all characters in the string are lower case
Answer: `print("dima1".islower()) # True`

Question: Given the string "DIMA1", write some code to determine whether all characters in the string are upper case
Answer: `print("DIMA1".isupper()) # True`

Question: Given the string "DIMA1", write some code to determine whether all characters in the string are upper case
Answer: `print("DIMA1".isupper()) # True`

Question: Given the string "    " (4 whitespace chars), write some code to determine whether all characters in the string are whitespace characters
Answer: `print("    ".isspace()) # True`

## strip, rstrip, lstrip, replace

Question: Given the string "    dima" (4 whitespace chars + "dima"), write some code to remove all whitespace characters and return string "dima"
Answer: `print("    dima".strip()) # "dima"`

Question: Given the string "    dima  " (4 whitespace chars + "dima" + 2 whitespace chars), write some code to remove whitespace characters before the substring "dima  "
Answer: `print("    dima  ".lstrip()) # "dima  "`

Question: Given the string "    dima  " (4 whitespace chars + "dima" + 2 whitespace chars), write some code to remove whitespace characters after the substring "    dima"
Answer: `print("    dima  ".rstrip()) # "    dima"`

Question: Given the string "dima Dima DIMA", write some code to replace all occurences of the substring "dima" replaced by "Olena"
Answer: `print("dima Dima dima".replace("dima", "Olena")) # "Olena Dima Olena"`

## split, find, rfind
Question: Given the string "dima_Dima_DIMA", write some code to convert it to a list of names ['dima', '', 'Dima', 'DIMA']
Answer: `print("dima__Dima_DIMA".split("_")) # ['dima', '', 'Dima', 'DIMA']`

Question: Given the string "dima_dima_dima", write some code to define the first index position of the substring "dima"
Answer: `print("dima_dima_dima".find("dima"))  # 0`

Question: Given the string "dima_dima_dima", write some code to define the last index position of the substring "dima"
Answer: `print("dima_dima_dima".rfind("dima"))  # 10`

# boolean vs. truthiness
https://launchschool.com/lessons/a29e9831/assignments/87263908

Question: Give 2 codes examples of short-circuiting behavior with logical operator `and`.
Answer: `and` short-circuits, stops evaluating when it encounters the first sub-expression from left-to-right that evaluates to `False`
```python
print(False and len(None))  # False
print([] and len(None))  # []


```

Question: Give 2 codes examples of short-circuiting behavior with logical operator `or`.
Answer: `or` short-circuits, stops evaluating when it encounters the first sub-expression from left-to-right that evaluates to `True`
```python
print(True and len(None))  # True
print("Dima" or len(None))  # Dima

```

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

# None
https://launchschool.com/books/python/read/data_types#none

Question: What is `None`?
Answer: `None` is a data type in Python used to express the absense of a value. It can also indicate missing or unavailable data.

# ranges
https://launchschool.com/books/python/read/data_types#sequences

Question: What is a `range`? Give a code example that demonstrates a range of odd integers starting a 1 and ending with 9.
Answer: A range is a sequence of integers between two endpoints. Ranges are most commonly used to iterate over an increasing or decreasing range of integers.
```python
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]

```

Question: Why does this code outputs `range(1, 10, 2)` and not a list of numbers `[1, 3, 5, 7, 9]`? Change the code to print the expected list of numbers.
```python
print(range(1, 10, 2))  # outputs "range(1, 10, 2)" not "[1, 3, 5, 7, 9]"

```
Answer: Python optimizes ranges to save memory. One way to get those numbers is to convert the range to a list or tuple. We can use the list and tuple functions to expand each range; either will suffice.
```python
odd_nums = list(range(1, 10, 2))
print(odd_nums)  # "[1, 3, 5, 7, 9]"

```

# list and dictionary syntax
Question: Write two distinct ways of reversing the list without mutating the original list.
```python
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

```
Answer: 
```python
reversed_numbers_one = numbers[::-1]
reversed_numbers_two = list(reversed(numbers))
```

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

Question: Given a list of numbers `[1, 2, 3, 4, 5]`, mutate the list by removing the number at index 2, so that the list becomes `[1, 2, 4, 5]`.
Answer: 
```python
numbers = [1, 2, 3, 4, 5]
del numbers[2]
print(numbers)  # [1, 2, 4, 5]
```

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

Question: Determine whether the following dictionary of people and their age contains an entry for 'Spot':
```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
```

Answer: 
```python
'Spot' in ages
```

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

Question: What will the following code output?
```python
print([1, 2, 3] + [4, 5])

```

Answer: In Python, you can use the `+` operator to concatenate two lists. This operation merges the second list into the first one, producing a new combined list.
```python
[1, 2, 3, 4, 5]

```

# list methods: len(list), list.append(), list.pop(), list.reverse()
Question: Given the list `elements = [0, 1 , 2]`, write some code to define its length
Answer: 
```python
print(len(elements))

```

Question: Given the list `elements = [0, 1 , 2]`, write some code to append string "Dima" to the end of sequence.
Answer: 
```python
elements = [0, 1, 2]
elements.append("Dima")
print(elements)  # [0, 1 , 2, "Dima"]

```

Question: Given the list `elements = [0, 1 , 2, "Dima"]`, write some code to remove string "Dima" from the end of sequence. Then remove element at index 1 from the sequence
Answer: 
```python
elements = [0, 1 , 2, "Dima"]
elements.pop()   # [0, 1 , 2]
elements.pop(1)  # [0, 2]
print(elements)  # [0, 2]

```

Question: Given the list `elements = [0, 1 , 2, "Dima"]`, write some code to reverse the items in place
Answer: 
```python
elements = [0, 1, 2, "Dima"]
elements.reverse()
print(elements)  # ['Dima', 2, 1, 0]

```

# dictionary methods: dict.keys(), dict.values(), dict.items()
Question: Given the dictionary 
```python
ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
}

```
write some code to return the list of the dictionary's keys.

Answer: 
```python
ages = {"dimo": 31, "olena": 32, "tetiana": 28}
names_from_ages = list(ages.keys()) # ages.keys() itself returns view object dict_keys(['dimo', 'olena', 'tetiana'])
print(names_from_ages)  # ['dimo', 'olena', 'tetiana']

```

Question: Given the dictionary 
```python
ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
}

```
write some code to return the list of the dictionary's values.

Answer: 
```python
ages = {"dimo": 31, "olena": 32, "tetiana": 28}
ages_list = list(
    ages.values()
)  # ages.values() itself returns view object dict_values([31, 32, 28])
print(ages_list)  # [31, 32, 28]

```

Question: Given the dictionary 
```python
ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
}

```
write some code to return the list of the dictionary's key value pairs.

Answer: 
```python
ages = {"dimo": 31, "olena": 32, "tetiana": 28}
ages_list = list(
    ages.items()
)  # ages.items() itself returns view object dict_items [('dimo', 31), ('olena', 32), ('tetiana', 28)]
print(ages_list)  # [('dimo', 31), ('olena', 32), ('tetiana', 28)]

```

# operators
https://launchschool.com/books/python/read/basic_ops#arithmeticoperations
## Arithmetic: +, -, *, /, //, %, **
Question: What will the following code return? Why? 
```python
print(16 // 3)     # 
print(16 // -3)    # 
print(16 // 2.3)   # 
print(-16 // 2.3)  # 

```
Answer: The // operator returns the largest whole number less than or equal to the floating point result. Thus, 16 // 3 returns 5, not 5.333333333333333. Likewise, 16 // -3 returns -6. If either operand is a float, the return value is also a float, but it's still rounded down to a whole number.

## String operators: +
## List operators: +
## Comparison: ==, !=, <, >, <=, >=
## Logical: and, or, not
## Identity: is, is not
## operator precedence



mutability and immutability
# Variables
Question: What will the code below output? 
```python
name = 'John'

def greet():
    print(f"Hello, {name}!")

greet()  # Output: ?? 

```
Answer: The `print` invocation prints string `"Hello, John!"`. The `name` variable is initialized in the global scope and is accessible within the `greet` function. 

Question: What will the code below output? 
```python
def my_func():
    local_var = 10
    print(local_var)

my_func()  # Output: ??
print(local_var)  # Output: ??

```
Answer: The `my_func()` invocation prints `10`. The `print` invocation with the variable name `local_var` passed as an argument raises `NameError: name 'local_var' is not defined`, because this variable is not accessible in the global scope. This code demostrates variable scope concept, specifically how variables defined in a function are local to that function and cannot be accessed in the outer scope.

Question: What will the code below output? 
```python
def my_func():
    global global_var
    global_var = 20

my_func()         # Output: ?? 
print(global_var) # Output: ?? 

```
Answer: The `my_func()` invocation returns `None`. The `print` invocation with the variable name `global_var` passed as an argument outputs `20`, because this variable is accessible in the global scope. The `global` keyword is used inside the `my_func` function to indicate that the `global_var` being modified is the global variable, not a local one. As a result, it is accessible outside of the function. This code demostrates variable scope concept, specifically how variables defined in a function are accessible globally if explicitly marked as `global`.

Question: What will the code below output? 
```python
outer_var = 15

def my_func():
    print(outer_var)

my_func()  # Output: ?? 

```
Answer: The `my_func()` invocation outputs `15`. The `outer_var` variable is used but not reassigned in the `my_func` function, so Python looks for it in the outer scope and successfully finds and reads the value 15. This code demostrates variable scope concept, specifically how functions can access variables from their containing scope unless those variables are redefined within the function.

Question: What will the code below output? 
```python
outer_var = 15


def my_func():
    global outer_var
    outer_var = 12
    print(outer_var)


my_func()  # Output: ??
print(outer_var)  # Output: ??

```
Answer: The `my_func()` invocation outputs `12`. The `print()` with the variable name `outer_var` passed as an argument outputs `12`. The `global` keyword is used inside the `my_func` function to explicitly indicate that the `outer_var` being reassigned is the global variable, not a local one. This code demostrates variable scope concept, specifically how functions can reassign the variables in global scope using the `global` keyword.

Question: What will the code below output? 
```python
def func_a():
    a = 'hello'
    print(a)

def func_b():
    print(a)  # Output: ??

func_a()
func_b()

```
Answer: Executing `print(a)` raises a `NameError: name 'a' is not definedsince` since variable `a` is not in scope in `func_b`. The assignment on line 2 defines a variable named `a`, but that variable's scope is limited to `func_a`. `func_b` cannot access the variable defined in `func_a`. This code demostrates variable scope concept, specifically how two variables with different local scopes do not conflict.

Question: What will the code below output? 
```python
if True:
    block_var = 'Hello'

print(block_var)  # Output: ??

```
Answer: Executing `print(block_var)` outputs `Hello`. `block_var` is initialized within the `if` block and can  be accessed outside of it. This code demostrates variable scope concept, specifically how variables defined within blocks, such as `if` statements, are accessible outside of those blocks in Python.

Question: What will the code below output? 
```python
for val in range(5):
    val = val + 1

print(val)  # Output: ??

```
Answer: Executing `print(val)` outputs `5`. `val` is initialized within the `for` loop block and can be accessed outside of it. After the loop has ended, the last value assigned to variable `val` is the sum of integers `4 + 1` or `5`. This code demostrates variable scope concept, specifically how variables defined within blocks, such as `for` loops, are accessible outside of those blocks in Python

This code demostrates variable scope concept, specifically how variables defined within blocks, such as `if` statements or loops, are accessible outside of those blocks in Python.


Question: What will the following code print and why?
```python
num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

```
Answer: Executing `print(num)` outputs `10`. The variable `num` is initialized to `5` on line 1. On line 4 we use `global` keyword inside the function to reference the global variable `num` initialized on line 1. For that reason, on line 5 we are reassigning global variable `num` to `10` and on line 8 printing that value.

Question: What will the following code print and why?
```python
def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

```
Answer: This prints `Hello World`. The `outer()` function defines a local variable `outer_var` with the value `'Hello'`. Inside it, the `inner()` function is defined, which has its own local variable `inner_var` with the value `'World'`. When `inner()` is called within `outer()`, both `outer_var` and `inner_var` are printed using `print(outer_var, inner_var)`, which outputs `Hello World`.


variables as pointers
Question: What specifically do we mean when we refer to a variable's scope?
Answer: We mean where in a program that variable is available for use.


✔️ variable shadowing
conditionals and loops
for
while
print() and input()
Functions:
definitions and calls
return values
parameters vs. arguments
https://launchschool.com/lessons/a29e9831/assignments/248a3cc6 

nested functions
output vs. return values, side effects

✔️ expressions and statements
Question: In the following code example, what is a statement and what is an expression? 
```python
my_name = "Dima"

```
Answer: 
- `my_number = 3` is a statement that assigns the value `3` to the variable `my_number`.
- The value `3` itself is an expression. (Code appearing to the right of an `=` in an assignment or reassignment is an expression.)

discuss a function's use and purpose (a "user-level" description) instead of its implementation
