print("========================While Loops========================")

i = 0
while i < 11:
    print("Value of i: ", i)

    i = int(input("Enter value of i: "))
else:
    print("Value of i ", i, " is now able to false while condition. ")

j = 1
while j > 0:
    print("Value of j: ", j)

    j = int(input("Enter value of i: "))
else:
    print("Value of j ", j, " is now able to false while condition. ")

# increment in python is use like i=i+1 instead of i++
k = 0
while k < 10:
    print("Value of k: ", k)
    k = k + 1
else:
    print("Value of k:", k, " is now able to false while condition")
# decrement in python is use like i=i-1 instead of i--
l = 5
while l > 0:
    print("Value of l: ", l)
    l = l - 1
else:
    print("Value of l:", l, " is now able to false while condition")
    
j=5
while j < 3:
    print("You are True!")
else:
    print("Loop condition is false.")
