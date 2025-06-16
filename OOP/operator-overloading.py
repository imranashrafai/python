print("======================== Operator Overloading ========================")


class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    # Overloading the add operator (+)
    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)


# Creating two Vector objects
v1 = Vector(12, 2, 17)
v2 = Vector(19, 3, 12)

# Printing the string representation of v1 and v2
print(str(v1))
print(str(v2))

# Adding v1 and v2 using the overloaded + operator
resultant = v1 + v2

# Printing the result and its type
print(resultant)
print(type(resultant))
