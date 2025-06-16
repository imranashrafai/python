print("========================Break and Continue statements========================")

# Break statement exit the loop
for i in range(12):
    if i == 9:
        break
    print("5 * ", i, " = ", 5 * i)
# Continue statement skip the specific iteration  also do not print anything which is written after contunue statement
print(end="\n")

for i in range(12):
    if i == 9:
        print("I skip", i, ":value")
        continue
    print("5 * ", i, " = ", 5 * i)
