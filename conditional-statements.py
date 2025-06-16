import time

print("========================Conditional Statements========================")

age = int(input("Enter Your Age! "))
# if-else
if age >= 18:
    print("You are eliggible for driving")
else:
    print("You are not eligible for driving.")
# if-else-if
if age >= 18:
    print("You are adult!")
elif age < 18 and age >= 12:
    print("You are teenager")
else:
    print("You are child.")
# nested-if
number = int(input(("enter number: ").title()))
if number % 2 == 0:
    print("Number is even")
    if number > 0:
        print("Numer is positive")
    else:
        print(("Number is negative").title())
else:
    print(("number is odd").title())
# printing time and greetings First of all import time module(Built In)
import time

timestamp = time.strftime("%H:%M:%S")
print("Current Time:", timestamp)

a = int(time.strftime("%H"))
if a >= 5 and a <= 12:
    print("Good Morning")
elif a > 12 and a <= 18:
    print("Good Afternoon!")
elif a > 18:
    print("Good Evening!")
else:
    print("Good Night!")
