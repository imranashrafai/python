print("========================Tupple========================")
# tupple cannot change and  mainted its order during printing and store multiple datatypes
tup = (12, 11, 3, 1, 4, "imran", True)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(tup[6])
print(len(tup))

# negative index => tupple[len[tupple]-3]
print(tup[-2])  # tupple[len[tupple]-3] => tupple[7-2]= tupple[5]


# searching in tupple to find element
if "imran" in tup:
    print("Yes")
else:
    print("No")


print(tup[1:4])

# append two tupples
tup1 = ("imran", "ashraf", "abdul", "mani")
tup2 = ("ali",)
tu = tup1 + tup2
print(tu)
# convert tupple to list and then list to tupple
t = ("imran", "ashraf", "abdul", "mani")
l = list(t)
l[3] = "bakhtu"
l.append("irfan")
l.append("rehan")
te = tuple(l)
print(te)

# loops in tuple
tap = (x * x for x in range(23) if x % 2 == 0)

for i in tap:
    print(i, end=" ")
