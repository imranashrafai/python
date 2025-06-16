print("========================Match Case Statement========================")
# Match case statement most similar to switch statement
operator = input("Enter Operator: ")
valFirst = int(input("Enter first value: "))
valSec = int(input("Enter second value: "))
result = None
match operator:
    case "+":
        result = valFirst + valSec
        print("Addition = ", result)
    case "-":
        result = valFirst - valSec
        print("Subbtraction = ", result)
    case "/":
        result = valFirst / valSec
        print("Division = ", result)
    case "%":
        result = valFirst % valSec
        print("Modulus = ", result)
    case "//":
        result = valFirst // valSec
        print("Floor Division = ", result)
    case "*":
        result = valFirst * valSec
        print("Multiplication = ", result)
    case "**":
        result = valFirst**valSec
        print("Exponentiation = ", result)
    case _:
        print("You entered wrong operation")

match result:
    case result if result < 300:
        print("Your result is less than 300 and Answer: ", result)
    case result if 300 <= result < 400:
        print("Your result is between 300-399 and Answer: ", result)
    case result if 400 <= result < 500:
        print("Your result is between 400-499 and Answer: ", result)
    case result if 500 <= result < 600:
        print("Your result is between 500-599 and Answer: ", result)
    case result if 600 <= result < 700:
        print("Your result is between 600-699 and Answer: ", result)
    case result if 700 <= result < 800:
        print("Your result is between 700-799 and Answer: ", result)
    case result if 800 <= result < 900:
        print("Your result is between 800-899 and Answer: ", result)
    case result if 900 <= result < 1000:
        print("Your result is between 900-999 and Answer: ", result)
    # default throws error message if choose wrong
    case _:
        print("Your result is grreater than 1000")
