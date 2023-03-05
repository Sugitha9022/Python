from replit import clear
from art import logo

# def calculation(f_name, next_name, operator):
#   if operator == "+":
#     return f_name + next_name
#   elif operator == "-":
#     return f_name - next_name
#   elif operator == "*":
#     return f_name * next_name
#   elif operator == "/":
#     return f_name / next_name
#   else:
#     return "Input a valid operator"


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def first_num():
    print(logo)
    num = float(input("What's the first num? "))
    for key in operations:
        print(key)
    return num


next_calc = True
f_name = first_num()

while next_calc:
    operator = input("Pick an operation: ")
    next_num = float(input("What's the next number: "))
    f_name = float(f_name)
    next_num = float(next_num)
    # result = calculation(f_name, next_num)
    result = operations[operator](f_name, next_num)
    print(f"{f_name} {operator} {next_num} = {result}")

    continue_calc = input(
        f"\nType 'yes' to continue calculating with {result}, or type 'no' to start a new calculation: "
    )
    if continue_calc == "yes":
        f_name = result
        next_calc = True
    else:
        clear()
        f_name = first_num()
