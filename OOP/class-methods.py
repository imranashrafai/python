print("======================== Class Methods ========================")


class Employee:
    # class variable
    companyName = "ZIAH"

    def show(self):
        print(f"Employee name is {self.name} and company name is {self.companyName}")

    # to change value of class variable then use this decorator
    @classmethod
    # cls refer to class
    def changeCompanyName(cls, newcompany):
        cls.companyName = newcompany


e1 = Employee()
e1.name = "EMU"
e1.show()
print(e1.companyName)
e1.changeCompanyName("Starlink")
e1.name = "Mani"
e1.show()
print(e1.companyName)
