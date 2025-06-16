print("======================== Inheritance ========================")


class Employee:
    def __init__(self):
        # private attribute
        self.__name = "Imran Ashraf"
        


# child class name(Parent Class Name)
class Child1(Employee):
    pass


a = Child1()
# private attribute can access like this:
print(a._Employee__name)





