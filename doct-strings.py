print("======================== Doc-strings & PEP-8 ========================")


# Written a string above the body of function it tells what is input and what will output
# used to for definition of classes,functions
def square(n):
    """
    This function takes n inputs and give square of n numbers
    """
    return n * 2


print(square(12))
# we can acces string => functionName.__doc__
print(square.__doc__)

print(
    "======================== PEP-8(Python Enhancement Purposal) ========================"
)

