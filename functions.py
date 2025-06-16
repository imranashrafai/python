print("========================Functions========================")

def calculateGM(a, b):
    mean = (a * b) / (a + b)
    print("GM of given numbers = ", mean)


def checkNum(a, b):
    if a > b:
        print("First number is grater than second")
    elif b > a:
        print("Second number is greater than first")
    else:
        print("both numbers are equal")


# first = int(input("Enter First value: "))
# second = int(input("Enter Second value: "))
# calculateGM(first, second)
# checkNum(first, second)


def noBody(a, b):
    pass


# Default arguments Functions
def arguFun(fname="imran", lname="ashraf"):
    print("Hello! ", fname, lname)


arguFun()
arguFun("Mani")
arguFun("Mani", "Jutt")


# Keywords arguments function : we can change order of arguments using key
def keywordFun(fname="mani", lname="jutt"):
    print("Greetings!", fname, lname)


keywordFun()
keywordFun(lname="Ashraf")
keywordFun(lname="Ashraf", fname="Imran")


# required arguments function
def requiredFun(fname, lname, age):
    print(fname, lname, "is", age, "years old.")


requiredFun("Imran", "Ashraf", 19)


# variable-length arguments functions (i) Arbitrary Arguments (ii) Keyword Arbitrary Arguments
# Arbitrary Arguments Functions: when infinte arguments need to pass then us this function
def avgNumsFun(*numbers):
    average = 0
    for i in numbers:
        average = average + i
    print("Average is: ", average / len(numbers))


avgNumsFun(12, 12, 2, 42, 12, 34, 5, 67, 87, 34, 23, 1)

# keyword Arbitrary argumnets will see in Lecture of Tuple


# return type functions
def avgNums(*numbers):
    average = 0
    for i in numbers:
        average = average + i
    return average / len(numbers)


result = avgNums(12, 12, 2, 42, 23, 4, 5, 4, 7, 5, 8, 98, 75, 53, 23, 12)
print("Average of Retunr type function: ", result)
