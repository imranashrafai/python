print("======================== Warlus Operator ========================")
# :=
name = True
print(name)


print(name := False)


li = list()
while (food := input("Enter name of food which are available in your home?")) != "quit":
    li.append(food)


for i in li:
    print(i)
