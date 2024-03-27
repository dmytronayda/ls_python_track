# Not fully understand
# my_var = [1]


# def my_func(my_var):
#     my_var = [2]


# my_func(my_var)
# print(my_var)  # Output: [1]


num = 5


def my_func():
    print(num)


my_func()

# This prints `5`.
# The variable `num` initialized in the global scope and assigned the value of integer 5.
# On line 16 the function name `my_func` is initialized. Its body on line 17 is read and saved in the heap.
# On line 19 function `my_func` is invoked.
# The line 17 is called with value of global `num`, integer 5 and printed to the console.


num = 5


def my_func():
    num = 10


my_func()
print(num)


# This prints `5`
# On line 29 variable `num` initialized in the global scope and assigned the value of integer 5.
# On line 32 function `my_func` is initialized. Its body on line 33 is read and saved in the heap.
# On line 36 function `my_func` is invoked.
# The line 33 is called with value of function-scope local variable `num` assigned the value of integer 10.
# On line 37 function `print` is invoked with value of global scope `num`, integer 5, and printed to the console.


num = 5


def my_func():
    global num
    num = 10


my_func()
print(num)


# This prints `10`
# On line 51 function `my_func` is initialized. Its body on lines 52-53 is read and saved in the heap.
# On line 56 function `my_func` is invoked.
# Line 52 `global` keyword tells the function to refer to the global variable `num`.
# On line 53, global `num` variable reassigned to value of integer 10
# On line 57, `print` function is invoked with latest value assigned to variable `num`, 10.


def outer():
    outer_var = "Hello"

    def inner():
        inner_var = "World"
        print(outer_var, inner_var)

    inner()


outer()

# This prints "Hello World"
# On line 68 function `outer` is defined. Its body on lines 69-75 is read and saved in the heap.
# On line 78 function `outer` is invoked.
# Local to the scope of `outer` function variable `outer_var` initialized and assigned the value of string "Hello"
# On line 71 function `inner` is defined. Its body on lines 72-73 is read and saved in the heap.
# On line 75 function `inner` is invoked.
# Local to the scope of `inner` function variable `inner_var` initialized and assigned the value of string "World"
# On line 57, `print` function is invoked with value assigned to variable `outer_var` and `inner_var`.
# Variable `outer_var` is accessible as it is in the outter / parent function scope.


def my_func():
    num = 10


my_func()
print(num)

# Code raises NameError: num is not defined


def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()  # "Inner 1: 25"
    inner_func2()  # "Inner 2: 15"


my_func()
