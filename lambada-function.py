print("========================Lambada Function========================")
# used to write small functions in single lines and use to pass to other functions as arguments
square = lambda x: x * x
print(square(12))


avg = lambda x, y, z: (x + y + z) / 3
print(avg(12, 33, 21))


def functofunc(percen, value):
    return percen(value) * 122


percen = lambda x: (x / x) * 100
functofunc(percen, 12)
