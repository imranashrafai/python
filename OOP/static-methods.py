print("======================== Static Methods ========================")


class Math:
    @staticmethod
    def show(name, age):
        print(f"Name of user is {name} and his age is {age}")


# In python static methods are called by class name refrence  (ClassName.Static_Method_name)
Math.show("Imran Ashraf", 19)
