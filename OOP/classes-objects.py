print("======================== Classes and objects ========================")


# defining class
class Student:
    name = "imran"
    fname = "ashraf"
    classofstd = "12"
    age = 9
    pocketmoney = 1200

    def info(self):
        self.name = input("Enter Your Name: ")
        self.fname = input("Enter Your Father Name: ")
        self.classofstd = input("Enter Your Class: ")
        self.age = int(input("Enter Your Age: "))
        self.pocketmoney = int(input("Enter Your Pocket money : "))
        print(
            f"Mr. {self.name} S/O {self.fname} is studing in class {self.classofstd} at the age of {self.age} and takes Rs.{self.pocketmoney} pocket money monthly."
        )


# creating object
std1 = Student()
std1.info()
