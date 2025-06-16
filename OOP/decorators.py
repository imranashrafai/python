print("======================== Decorators ========================")
# too complex but very important and usefull in python


def decorator(fun):
    def greetings(*args, **kwargs):
        print("Good Afternoon Sir!")
        result = fun(*args, **kwargs)

        print("Your required Answer is:", result)

    return greetings


# write function name with sign @
@decorator
def add(a, b):
    return a + b


add(12, 3)


def myfun(func):
    def welcome(*args, **kwargs):
        print("Welcome to Simple Calculator!")
        a = func(*args, **kwargs)
        print("Your Result is :", a)
        print("Good Bye!")

    return welcome


@myfun
def calculator(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "/":
        return a / b
    elif op == "*":
        return a * b
    else:
        print("You entered wrong")
        return None


calculator(12, "//", 6)
