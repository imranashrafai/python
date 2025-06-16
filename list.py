print("========================List========================")
# list can change and  mainted its order during printing and store multiple datatypes
lest = [12, 11, 3, 1, 4, "imran", True]
print(lest[0])
print(lest[1])
print(lest[2])
print(lest[3])
print(lest[4])
print(lest[5])
print(lest[6])
print(len(lest))

# negative index => list[len[list]-3]
print(lest[-2])  # list[len[list]-3] => list[7-2]= list[5]


# searching in list to find element
if "imran" in lest:
    print("Yes")
else:
    print("No")
# search in string
if "ran" in "imran":
    print("Yes")
else:
    print("Nah")
# print whole list
print(lest[:])
print(lest[: len(lest)])
print(lest[0 : len(lest)])

# print list by jumping => list[start: end: jumpIndex]

print(lest[0 : len(lest) : 3])

# list comprehension
fruits = ["apple", "bannana", "orange", "grapes", "chilli"]
li = [x for x in fruits if "a" in x]
print(li)
numbers = [x * x for x in range(30) if x % 2 == 0]
print(numbers)

# list Methods
lis = [3, 212, 3, 5, 7, 8, 9, 10, 2, 11, 2, 32, 12, 2, 2]
print(lis)
# Add element at the end of list
lis.append(1)
print(lis)
# sort elements in Ascending orders
lis.sort()
print(lis)
# sort elements in Decending orders
lis.sort(reverse=True)
print(lis)
# reverse the orginal list elements
lis.reverse()
print(lis)
# return the index of given element
print(lis.index(7))
# return number of elements in a list
print(lis.count(2))
# make copy of list and if i wanna change then change will be in original list and copy lis will be original
listMy = ["apple", "grapes", "cherry", "guava", "mango"]
copyList = listMy.copy()
copyList[0] = "imran"
print(copyList)
print(listMy, "\n")
# list function does same
MyList = ["apple", "grapes", "cherry", "guava", "mango"]
copyMyList = list(MyList)
copyMyList[2] = "imran ashraf"
print(copyMyList)
print(MyList, "\n")

# change both listsٖ
PgList = ["apple", "grapes", "cherry", "guava", "mango"]
newList = PgList
newList[4] = "peach"
print(newList)
print(PgList)

# insert element in list by given index
myli = [2, 1, 3, 4, 5, 22, 56, 7, 88]
myli.insert(2, 324)
print(myli)
# insert at the end of list
nl = [2, 1, 3, 4, 5, 22, 56, 7, 88]
enL = [200, 300, 400, 500]
nl.extend(enL)
print(nl,"\n")
# merge two lists without changing in original list
l = [1, 2, 3, 4, 5, 6]
m = [7, 8, 9]
k = l + m
print(k)
print(l)
