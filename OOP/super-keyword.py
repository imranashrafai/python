print("======================== Super Keyword ========================")


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"Name of employee is {self.name} and id is {self.id}", end=" ")


class Programmer(Employee):
    def __init__(self, name, id, lang, age):
        super().__init__(name, id)
        self.lang = lang
        self.age = age

    def show(self):
        super().show()
        print(f"and specialized in {self.lang} and his age is {self.age}.")


imran = Programmer("Imran Ashraf", "1201", "Python & java", 19)
imran.show()
