False or (True and False) # False
True or (1 + 2)           # True
(1 + 2) or True           # Returns 3 due short circuiting: int 3 is a truthy value second value in the OR statetement is disregarded
True and (1 + 2)          # Returns 3, as it was the last operand checked by Python
False and (1 + 2)         # False
(1 + 2) and True          # True
(32 * 4) >= 129           # False
False != (not True)       # False
True == 4                 # False
False == (847 == '847')   # True

# my solution
# def even_or_odd(n):
#     if n % 2 == 0:
#         return "even"
#     return "odd"

def even_or_odd(n):
    return("even" if n % 2 == 0 else "odd")

# print(even_or_odd(3)); # odd
# print(even_or_odd(8)); # even

def capitalize(copy):
    return(copy.upper() if len(copy) > 10 else copy)

# print(capitalize("hello world")) #'HELLO WORLD'
# print(capitalize("goodbye"))     #'goodbye'

def number_range(integer_num):
    if integer_num < 0:
        return f"{integer_num} is less than 0"
    elif integer_num <= 50:
        return f"{integer_num} is between 0 and 50"
    elif integer_num <= 100:
        return f"{integer_num} is between 51 and 100"
    else:
        return f"{integer_num} is greater than 100"
    

print(number_range(0))     # 0 is between 0 and 50
print(number_range(25))    # 25 is between 0 and 50
print(number_range(50))    # 50 is between 0 and 50
print(number_range(75))    # 75 is between 51 and 100
print(number_range(100))   # 100 is between 51 and 100
print(number_range(101))   # 101 is greater than 100
print(number_range(-1))    # -1 is less than 0    