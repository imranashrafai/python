print("======================== Setter and Getter Functions ========================")


class Myclass:
    # initializer (Parameterized Constructor)
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter
    def get_name(self):
        return self._name

    # setter
    def set_name(self, name):
        self._name = name

    # getter
    def get_age(self):
        return self._age

    # setter
    def set_age(self, age):
        self._age = age


std = Myclass("Imran Ashraf", 17)
std.set_name("M. Imran Ashraf")
std.set_age(19)
print("Updated Name is: ", std.get_name())
print("Updated Age is: ", std.get_age())
