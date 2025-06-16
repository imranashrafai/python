print("======================== Constructor ========================")


class Employee:
    # parameterized constructor
    def __init__(self, emname=None, emfname=None, embps=None, age=None, emsalary=None):
        # python run the last constructor if declare more than one, to run default construnctor then use it:
        # default Constructor
        if (
            emname is None
            and emname is None
            and embps is None
            and age is None
            and emsalary is None
        ):
            print("I am Default Constructor!")
        else:
            self.emname = emname
            self.emfname = emfname
            self.embps = embps
            self.age = age
            self.emsalary = emsalary
            print(
                f"Mr. {self.emname} S/O Mr. {self.emfname} has BPS-{embps} with Rs.{emsalary} salary at the age of {age}"
            )


a = Employee("Imran Ashraf", "Ashraf Yaseen Tabassum", 16, 19, 90000)
b = Employee()
