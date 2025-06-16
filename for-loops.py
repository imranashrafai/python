print("========================For Loops========================")

# range function take three parameters first is start , 2nd is end and third is step (increment)
name = "imranashraf "
list = ["imran", "ashraf", "yaseen", "tabbassum"]

for i in name:
    print(i, end=" ")
print()

for i in list:
    print(i)

for i in range(300):
    print(i, end=" ")

print()
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print("\n")
rows = 5
cols = 8

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n")
# in this incrementing number by 2

for i in range(1, 16, 2):
    print(i)



table = int(input("Enter table you wanna printout: "))
end = int(input("Enter value where you want to end table: "))
for i in range(1, end + 1):
    result = table * i
    print(table, " * ", i, " = ", result)



