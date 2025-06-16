print("======================== Exception Handling ========================")

try:
    table = input("Enter number of table to print: ")
    for i in range(1, 11):
        print(f"{int(table)} * {i} = {int(table)*i}")
    li = [1, 2, 3]
    ind = int(input("Enter index to access element: "))
    print(li[ind])


except ValueError:
    print("Input Error Occured!")

except IndexError:
    print("Index Error Occured!")


# or we can simple use print statement to show custom error like this
# except:
#     print("Input error occured!")
