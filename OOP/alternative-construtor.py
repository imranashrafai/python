print(
    "======================== Class Methods as Alternative Constructors ========================"
)
# use to do enhacement in constructor and returns an object


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def strFrom(cls, string):
        parts = string.split("-")
        if len(parts) == 2:
            return cls(parts[0], parts[1])
        else:
            raise ValueError(
                "Input string must contain exactly two elements separated by '-'."
            )


# Creating an Employee instance using the default constructor
e1 = Employee("Imran", 23)
print(e1.name, e1.age)
# Creating an Employee instance using the alternative constructor (class method)

st = "Imran Ashraf-19"
e2 = Employee.strFrom(st)
print(e2.name, e2.age)  # Output: Imran Ashraf 19
