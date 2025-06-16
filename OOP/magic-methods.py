print("======================== Dunder/Magic Methods ========================")


class Employee:
    name = "Imran Ashraf"

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self):
        return f"name of employee is {self.name}"

    def __repr__(self):
        return f"Employee('{self.name}')"

    def __call__(self):
        print("Hey I am good")


e = Employee()
print(len(e))
print(str(e))
print(repr(e))
e()
